from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import mapped_column, Mapped, relationship
from enum import Enum
from sqlalchemy import Enum as SqlEnum, Date
from app.models.base import Base
from app.models.teacher import Teacher
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User

class Employee_Type(str, Enum):
    TEACHER = "teacher"
    PRINCIPAL = "principal"
class Employee(Base):
    __tablename__ = "employee"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    user: Mapped["User"] = relationship(back_populates="employee")
    teacher: Mapped["Teacher"] = relationship(back_populates="employee")
    employee_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    hire_date: Mapped[Date] = mapped_column(Date, nullable=False)
    employee_type: Mapped[Employee_Type] = mapped_column(SqlEnum(Employee_Type), nullable=True)
    