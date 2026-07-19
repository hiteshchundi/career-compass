from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
}


@dataclass(slots=True)
class SavedFile:
    """
    Represents a successfully saved uploaded file.
    """

    original_filename: str
    stored_filename: str
    file_path: str
    file_type: str


def save_upload_file(file: UploadFile) -> SavedFile:
    """
    Save an uploaded file to disk.

    Args:
        file: Uploaded file received from FastAPI.

    Returns:
        A SavedFile instance containing metadata about the saved file.

    Raises:
        ValueError:
            If the uploaded file type is not supported.
    """

    if not file.filename:
        raise ValueError("Uploaded file has no filename.")

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    stored_filename = f"{uuid4()}{extension}"

    destination = UPLOAD_DIR / stored_filename

    with destination.open("wb") as buffer:
        buffer.write(file.file.read())

    return SavedFile(
        original_filename=file.filename,
        stored_filename=stored_filename,
        file_path=str(destination),
        file_type=extension.lstrip("."),
    )