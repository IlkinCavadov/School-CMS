from app.models.user import User
from sqlalchemy import select
from sqlalchemy.orm import Session

def email_exists(db: Session, email: str) -> bool:
    stmt = select(User).where(User.email == email)
    result = db.execute(stmt)
    return result.scalars().one_or_none() is not None


def username_exists(db: Session, username: str) -> bool:
    stmt = select(User).where(User.username == username)
    result = db.execute(stmt)
    return result.scalars().one_or_none() is not None

def create(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str) -> User:
    stmt = select(User).where(User.email == email)
    result = db.execute(stmt)
    return result.scalars().one_or_none()

def get_user_by_username(db: Session, username: str) -> User:
    stmt = select(User).where(User.username == username)
    result = db.execute(stmt)
    return result.scalars().one_or_none()
