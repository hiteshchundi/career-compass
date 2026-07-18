from app.db.models.resume import Resume
from app.db.repositories.resume_repository import ResumeRepository
from app.services.base_service import BaseService


class ResumeService(BaseService[ResumeRepository]):
    def create_resume(
        self,
        *,
        user_id: int,
        filename: str,
        file_path: str,
        file_type: str,
        content: str,
    ) -> Resume:
        db_resume = Resume(
            user_id=user_id,
            filename=filename,
            file_path=file_path,
            file_type=file_type,
            content=content,
        )

        return self.repository.create(db_resume)

    def get_resume(self, resume_id: int) -> Resume | None:
        return self.repository.get_by_id(resume_id)

    def get_user_resumes(self, user_id: int) -> list[Resume]:
        return self.repository.get_by_user(user_id)