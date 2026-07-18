from sqlalchemy.orm import Session

from app.db.models.analysis import Analysis
from app.db.repositories.base import BaseRepository


class AnalysisRepository(BaseRepository[Analysis]):
    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_resume(self, resume_id: int) -> list[Analysis]:
        return (
            self.db.query(Analysis)
            .filter(Analysis.resume_id == resume_id)
            .all()
        )

    def get_by_job(self, job_id: int) -> list[Analysis]:
        return (
            self.db.query(Analysis)
            .filter(Analysis.job_id == job_id)
            .all()
        )