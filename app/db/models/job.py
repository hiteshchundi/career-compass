from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(255))
    company: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)

    analyses: Mapped[list["Analysis"]] = relationship(
        "Analysis",
        back_populates="job",
        cascade="all, delete-orphan",
    )