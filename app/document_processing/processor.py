from fastapi import UploadFile

from app.ingestion.extractors import EXTRACTORS
from app.ingestion.normalizer import normalize_text
from app.utils.file_storage import save_upload_file


class DocumentProcessor:
    """
    Shared document processing pipeline.

    Responsibilities:
    - Save uploaded file
    - Extract text
    - Normalize text
    """

    @staticmethod
    def process(file: UploadFile):
        saved_file = save_upload_file(file)

        try:
            extractor = EXTRACTORS[saved_file.file_type]
        except KeyError as exc:
            raise ValueError(
                f"Unsupported file type: {saved_file.file_type}"
            ) from exc

        extracted_text = extractor(saved_file.file_path)

        normalized_text = normalize_text(extracted_text)

        return saved_file, normalized_text