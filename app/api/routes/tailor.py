from pathlib import Path
import shutil
import tempfile

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse

from app.ingestion.docx import extract_text as extract_docx_text
from app.ingestion.pdf import extract_text as extract_pdf_text

from app.ai.llm_service import LLMService
from app.ai.docx_generator import ResumeGenerator

router = APIRouter(
    prefix="/tailor",
    tags=["Tailor Resume"],
)


@router.post("")
async def tailor_resume(
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
        # ----------------------------
        # Extract Resume Text
        # ----------------------------
        if suffix == ".pdf":
            resume_text = extract_pdf_text(temp_path)
        else:
            resume_text = extract_docx_text(temp_path)

        # ----------------------------
        # Generate AI Tailored Resume
        # ----------------------------
        tailored_resume = LLMService().tailor_resume(
            resume_text=resume_text,
            job_description=job_description,
        )

        # ----------------------------
        # Create DOCX
        # ----------------------------
        output_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".docx",
        )

        output_file.close()

        ResumeGenerator.generate(
            tailored_resume,
            output_file.name,
        )

        return FileResponse(
            path=output_file.name,
            filename="tailored_resume.docx",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

    finally:
        temp_path.unlink(missing_ok=True)