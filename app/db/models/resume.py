from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )

    filename: Mapped[str] = mapped_column(
        String(255),
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
    )

    file_type: Mapped[str] = mapped_column(
        String(20),
    )

    content: Mapped[str] = mapped_column(
        Text,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="resumes",
    )

    analyses: Mapped[list["Analysis"]] = relationship(
        "Analysis",
        back_populates="resume",
        cascade="all, delete-orphan",
    )