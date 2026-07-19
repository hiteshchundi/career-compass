from fastapi import UploadFile

from app.db.models.resume import Resume
from app.ingestion.extractors import EXTRACTORS
from app.ingestion.normalizer import normalize_text
from app.repositories.resume_repository import ResumeRepository
from app.services.base_service import BaseService
from app.utils.file_storage import save_upload_file


class ResumeService(BaseService[ResumeRepository]):
    """
    Handles resume upload and retrieval.
    """

    def upload_resume(
        self,
        *,
        user_id: int,
        file: UploadFile,
    ) -> Resume:
        """
        Upload a resume, extract its text, normalize it,
        and persist it to the database.
        """

        saved_file = save_upload_file(file)

        try:
            extractor = EXTRACTORS[saved_file.file_type]
        except KeyError as exc:
            raise ValueError(
                f"Unsupported file type: {saved_file.file_type}"
            ) from exc

        extracted_text = extractor(saved_file.file_path)

        normalized_text = normalize_text(extracted_text)

        resume = Resume(
            user_id=user_id,
            original_filename=saved_file.original_filename,
            stored_filename=saved_file.stored_filename,
            file_path=saved_file.file_path,
            file_type=saved_file.file_type,
            extracted_text=normalized_text,
        )

        return self.repository.create(resume)

    def get_resume(
        self,
        resume_id: int,
    ) -> Resume | None:
        return self.repository.get_by_id(resume_id)

    def list_user_resumes(
        self,
        user_id: int,
    ) -> list[Resume]:
        return self.repository.list_by_user(user_id)