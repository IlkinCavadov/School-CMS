from app.models.role import Role
from sqlalchemy import select
from sqlalchemy.orm import Session

def role_exists(db: Session, role_name: str) -> bool:
    stmt = select(Role).where(Role.name == role_name)
    result = db.execute(stmt)
    return result.scalars().one_or_none() is not None

def create(db: Session, role: Role) -> Role:
    db.add(role)
    db.commit()
    db.refresh(role)
    return role
def get_role_by_name(db: Session, role_name: str) -> Role:
    stmt = select(Role).where(Role.name == role_name)
    result = db.execute(stmt)
    return result.scalars().one_or_none()