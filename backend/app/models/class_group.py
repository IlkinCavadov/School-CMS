from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.school_class import SchoolClass


class ClassGroup(Base):
    __tablename__ = "class_group"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    school_classes: Mapped[list["SchoolClass"]] = relationship(
        back_populates="class_group"
    )