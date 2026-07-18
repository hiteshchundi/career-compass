from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
}


def save_upload_file(file: UploadFile) -> tuple[str, str]:
    """
    Save an uploaded file and return:
    (saved_path, file_extension)
    """

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    unique_name = f"{uuid4()}{extension}"

    destination = UPLOAD_DIR / unique_name

    with destination.open("wb") as buffer:
        buffer.write(file.file.read())

    return str(destination), extension.replace(".", "")