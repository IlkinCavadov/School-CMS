from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.models.base import Base
from app.models.class_group import ClassGroup
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.teacher import Teacher
    


class SchoolClass(Base):
    __tablename__ = "school_class"

    id: Mapped[int] = mapped_column(primary_key=True)

    class_group_id: Mapped[int] = mapped_column(ForeignKey("class_group.id"), nullable=False)

    grade: Mapped[int] = mapped_column( Integer, nullable=False)

    school_year: Mapped[str] = mapped_column(String(9),nullable=False)

    home_teacher_id: Mapped[int | None] = mapped_column(ForeignKey("teacher.user_id"), nullable=True)

    class_group: Mapped["ClassGroup"] = relationship(back_populates="school_classes")

    home_teacher: Mapped["Teacher | None"] = relationship()