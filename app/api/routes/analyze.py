from pathlib import Path
import shutil
import tempfile

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.ingestion.docx import extract_text as extract_docx_text
from app.ingestion.pdf import extract_text as extract_pdf_text

from app.resume_analysis.parser import ResumeParser
from app.job_analysis.parser import JobParser
from app.matching.engine import MatchingEngine

from app.ai.llm_service import LLMService

router = APIRouter(
    prefix="/analyze",
    tags=["Analysis"],
)


@router.post("")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
):
    if not resume.filename:
        raise HTTPException(
            status_code=400,
            detail="Resume is required.",
        )

    suffix = Path(resume.filename).suffix.lower()

    if suffix not in {".pdf", ".docx"}:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX resumes are supported.",
        )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp_file:
        shutil.copyfileobj(resume.file, temp_file)
        temp_path = Path(temp_file.name)

    try:
        # --------------------------------------------------
        # Extract Resume Text
        # --------------------------------------------------
        if suffix == ".pdf":
            resume_text = extract_pdf_text(temp_path)
        else:
            resume_text = extract_docx_text(temp_path)

        # --------------------------------------------------
        # Parse Resume
        # --------------------------------------------------
        resume_data = ResumeParser().parse(resume_text)

        # --------------------------------------------------
        # Parse Job Description
        # --------------------------------------------------
        job_data = JobParser().parse(job_description)

        # --------------------------------------------------
        # Rule-Based Analysis
        # --------------------------------------------------
        baseline_result = MatchingEngine().compare(
            resume_data,
            job_data,
        )

        # --------------------------------------------------
        # AI Enhancement
        # --------------------------------------------------
        try:
            ai_result = LLMService().analyze(
                resume_text=resume_text,
                job_description=job_description,
                baseline_result=baseline_result,
            )

            return ai_result

        except Exception as e:
            print("\n========== LLM FAILED ==========")
            print(e)
            print("===================================\n")

            # Fall back to deterministic analysis
            return baseline_result

    finally:
        temp_path.unlink(missing_ok=True)