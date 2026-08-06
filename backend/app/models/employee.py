from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import mapped_column, Mapped
from app.models.base import Base
from datetime import datetime


class Employee(Base):
    __tablename__ = "employee"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    employee_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    hire_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    