from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.employee import Employee


class Teacher(Base):
    __tablename__ = "teacher"

    user_id: Mapped[int] = mapped_column(ForeignKey("employee.user_id"), primary_key=True)
    employee: Mapped["Employee"] = relationship(back_populates="teacher")
    
