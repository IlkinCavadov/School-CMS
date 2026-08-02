from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from app.models.base import Base



class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)