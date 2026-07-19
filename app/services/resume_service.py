from fastapi import UploadFile

from app.db.models.resume import Resume
from app.db.repositories.resume_repository import ResumeRepository
from app.services.base_service import BaseService
from app.document_processing.processor import DocumentProcessor


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

        saved_file, normalized_text = DocumentProcessor.process(file)

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