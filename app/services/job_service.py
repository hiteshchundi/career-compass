from app.db.models.job import Job
from app.db.repositories.job_repository import JobRepository
from app.schemas.job import JobCreate
from app.services.base_service import BaseService


class JobService(BaseService[JobRepository]):
    def create_job(self, job: JobCreate) -> Job:
        db_job = Job(
            title=job.title,
            company=job.company,
            description=job.description,
        )

        return self.repository.create(db_job)

    def get_job(self, job_id: int) -> Job | None:
        return self.repository.get_by_id(job_id)

    def get_all_jobs(self):
        return self.repository.get_all()