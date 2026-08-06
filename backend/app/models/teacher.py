from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import mapped_column, Mapped
from app.models.base import Base
from datetime import datetime


class Teacher(Base):
    __tablename__ = "teacher"

    user_id: Mapped[int] = mapped_column(ForeignKey("employee.user_id"), primary_key=True)
    
