from app.db.models.analysis import Analysis
from app.db.repositories.analysis_repository import AnalysisRepository
from app.schemas.analysis import AnalysisCreate
from app.services.base_service import BaseService


class AnalysisService(BaseService[AnalysisRepository]):
    def create_analysis(self, analysis: AnalysisCreate) -> Analysis:
        db_analysis = Analysis(
            resume_id=analysis.resume_id,
            job_id=analysis.job_id,
            score=analysis.score,
            feedback=analysis.feedback,
        )

        return self.repository.create(db_analysis)

    def get_resume_analyses(self, resume_id: int):
        return self.repository.get_by_resume(resume_id)

    def get_job_analyses(self, job_id: int):
        return self.repository.get_by_job(job_id)