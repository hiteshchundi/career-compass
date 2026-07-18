from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id: Mapped[int] = mapped_column(primary_key=True)

    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id")
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id")
    )

    match_score: Mapped[float] = mapped_column(
        Float
    )

    missing_skills: Mapped[str]

    recommendations: Mapped[str]