from pathlib import Path
import shutil
import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.ingestion.docx import extract_text as extract_docx_text
from app.ingestion.pdf import extract_text as extract_pdf_text
from app.resume_analysis.parser import ResumeParser

router = APIRouter(
    prefix="/resume-analysis",
    tags=["Resume Analysis"],
)


@router.post("")
async def analyze_resume(
    file: UploadFile = File(...),
):
    """
    Upload a resume and return a structured analysis.
    """

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided.",
        )

    suffix = Path(file.filename).suffix.lower()

    if suffix not in {".pdf", ".docx"}:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported.",
        )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_path = Path(temp_file.name)

    try:
        if suffix == ".pdf":
            text = extract_pdf_text(temp_path)
        else:
            text = extract_docx_text(temp_path)

        parser = ResumeParser()

        analysis = parser.parse(text)

        return analysis

    finally:
        temp_path.unlink(missing_ok=True)