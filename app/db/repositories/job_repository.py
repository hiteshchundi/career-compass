from sqlalchemy.orm import Session

from app.db.models.job import Job
from app.db.repositories.base import BaseRepository


class JobRepository(BaseRepository[Job]):
    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_id(self, job_id: int) -> Job | None:
        return (
            self.db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

    def get_all(self) -> list[Job]:
        return self.db.query(Job).all()