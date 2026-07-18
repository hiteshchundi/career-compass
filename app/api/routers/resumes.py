from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)

from app.utils.file_storage import save_upload_file

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)


@router.post("/upload")
def upload_resume(
    file: UploadFile = File(...),
):
    try:
        file_path, file_type = save_upload_file(file)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    return {
        "filename": file.filename,
        "file_path": file_path,
        "file_type": file_type,
    }