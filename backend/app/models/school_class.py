from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import mapped_column, Mapped
from app.models.base import Base
from datetime import datetime


class SchoolClass(Base):
    __tablename__ = "school_class"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_year: Mapped[int] = mapped_column(nullable=False)
    end_year: Mapped[int] = mapped_column(nullable=False)
    home_teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.user_id"), nullable=True)
