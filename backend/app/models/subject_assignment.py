from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import mapped_column, Mapped
from app.models.base import Base
from datetime import datetime


class SubjectAssignment(Base):
    __tablename__ = "subject_assignment"

    subject_id: Mapped[int] = mapped_column(ForeignKey("subject.id"), primary_key=True)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.user_id"), primary_key=True)
    