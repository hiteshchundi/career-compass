from sqlalchemy.orm import Session

from app.db.models.resume import Resume
from app.repositories.base_repository import BaseRepository


class ResumeRepository(BaseRepository[Resume]):
    """
    Repository responsible for Resume persistence.
    """

    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, resume: Resume) -> Resume:
        """
        Persist a new resume.
        """

        self.db.add(resume)
        self.db.commit()
        self.db.refresh(resume)

        return resume

    def get_by_id(self, resume_id: int) -> Resume | None:
        """
        Retrieve a resume by its ID.
        """

        return (
            self.db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

    def list_by_user(self, user_id: int) -> list[Resume]:
        """
        Retrieve all resumes belonging to a user.
        """

        return (
            self.db.query(Resume)
            .filter(Resume.user_id == user_id)
            .order_by(Resume.created_at.desc())
            .all()
        )

    def delete(self, resume: Resume) -> None:
        """
        Delete a resume.
        """

        self.db.delete(resume)
        self.db.commit()