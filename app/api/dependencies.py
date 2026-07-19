from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.repositories.analysis_repository import AnalysisRepository
from app.db.repositories.job_repository import JobRepository
from app.db.repositories.resume_repository import ResumeRepository
from app.db.repositories.user_repository import UserRepository
from app.db.session import SessionLocal
from app.services.analysis_service import AnalysisService
from app.services.job_service import JobService
from app.services.resume_service import ResumeService
from app.services.user_service import UserService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db    
    finally:
        db.close()


def get_user_repository(
    db: Session = Depends(get_db),
) -> UserRepository:
    return UserRepository(db)


def get_resume_repository(
    db: Session = Depends(get_db),
) -> ResumeRepository:
    return ResumeRepository(db)


def get_job_repository(
    db: Session = Depends(get_db),
) -> JobRepository:
    return JobRepository(db)


def get_analysis_repository(
    db: Session = Depends(get_db),
) -> AnalysisRepository:
    return AnalysisRepository(db)

def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repository)


def get_resume_service(
    repository: ResumeRepository = Depends(get_resume_repository),
) -> ResumeService:
    return ResumeService(repository)


def get_job_service(
    repository: JobRepository = Depends(get_job_repository),
) -> JobService:
    return JobService(repository)


def get_analysis_service(
    repository: AnalysisRepository = Depends(get_analysis_repository),
) -> AnalysisService:
    return AnalysisService(repository)