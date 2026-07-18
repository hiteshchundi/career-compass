from sqlalchemy.orm import Session

from app.db.models.resume import Resume
from app.db.repositories.base import BaseRepository


class ResumeRepository(BaseRepository[Resume]):
    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_id(self, resume_id: int) -> Resume | None:
        return (
            self.db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

    def get_by_user(self, user_id: int) -> list[Resume]:
        return (
            self.db.query(Resume)
            .filter(Resume.user_id == user_id)
            .all()
        )