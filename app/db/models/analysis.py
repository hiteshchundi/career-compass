from sqlalchemy import ForeignKey, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE")
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id", ondelete="CASCADE")
    )

    score: Mapped[float] = mapped_column(Float)

    feedback: Mapped[str] = mapped_column(Text)

    resume: Mapped["Resume"] = relationship(
        "Resume",
        back_populates="analyses",
    )

    job: Mapped["Job"] = relationship(
        "Job",
        back_populates="analyses",
    )