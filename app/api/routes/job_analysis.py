from pathlib import Path
import shutil
import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.ingestion.extractors import EXTRACTORS
from app.job_analysis.parser import JobParser

router = APIRouter(
    prefix="/job-analysis",
    tags=["Job Analysis"],
)


@router.post("")
async def analyze_job(
    file: UploadFile = File(...),
):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided.",
        )

    suffix = Path(file.filename).suffix.lower().lstrip(".")

    if suffix not in EXTRACTORS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX and TXT files are supported.",
        )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f".{suffix}",
    ) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_path = Path(temp_file.name)

    try:
        text = EXTRACTORS[suffix](temp_path)

        parser = JobParser()

        return parser.parse(text)

    finally:
        temp_path.unlink(missing_ok=True)