from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.models.base import Base
from app.models.school_class import SchoolClass
from app.models.student import Student
from datetime import datetime


class StudentHistory(Base):
    __tablename__ = "student_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("student.id"), nullable=False)
    student_class_id: Mapped[int] = mapped_column(ForeignKey("school_class.id"), nullable=False)
    school_year: Mapped[str] = mapped_column(String(9), nullable=False)
    student: Mapped["Student"] = relationship()
    student_class: Mapped["SchoolClass"] = relationship()
    
    
