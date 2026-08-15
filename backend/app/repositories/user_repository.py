from sqlalchemy import select, update
from sqlalchemy.orm import Session, selectinload

from app.models.user import User
from app.models.employee import Employee
from app.models.role import Role
from app.schemas.auth import UserUpdate


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


def get_user_by_id(db: Session, user_id: int) -> User | None:
    stmt = (
        select(User)
        .where(User.id == user_id)
        .options(
            selectinload(User.role),
            selectinload(User.employee),
        )
    )
    result = db.execute(stmt)
    return result.scalars().one_or_none()


def get_teacher(db: Session, user_id: int) -> User | None:
    stmt = (
        select(User)
        .where(User.id == user_id)
        .options(
            selectinload(User.role),
            selectinload(User.employee).selectinload(Employee.teacher),
        )
    )
    result = db.execute(stmt)
    return result.scalars().one_or_none()


def get_employee(db: Session, user_id: int) -> User | None:
    stmt = (
        select(
            
            User.first_name,
            User.last_name,
            User.username,
            User.email,
            Employee.employee_type,
            Role.name.label("role"),
            )
         .outerjoin(User.employee)
         .join(User.role)   
        .where(User.id == user_id)

    )
    result = db.execute(stmt)
    return result.mappings().one_or_none()


def get_employees(db: Session):
    stmt = (
        select(
            User.id,
            User.first_name,
            User.last_name,
            User.username,
            User.email,
            User.is_active,
            Employee.employee_type,
        )
        .join(User.employee)
        .join(User.role)
        .where(User.is_active.is_(True))
        .order_by(User.first_name, User.last_name)
    )

    result = db.execute(stmt)

    return result.mappings().all()


def update_user(db: Session, user_id: int, user_data: UserUpdate) -> User | None:
    values = user_data.model_dump(exclude_unset=True)

    if values:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(**values)
        )
        db.execute(stmt)
        db.commit()

    return get_user_by_id(db, user_id)


def deactivate_user(db: Session, user_id: int) -> User | None:
    stmt = (
        update(User)
        .where(User.id == user_id)
        .values(is_active=False)
    )
    db.execute(stmt)
    db.commit()

    return get_user_by_id(db, user_id)


def get_user_by_email(db: Session, email: str) -> User | None:
    stmt = (
        select(User)
        .where(User.email == email)
        .options(
            selectinload(User.role),
            selectinload(User.employee),
        )
    )
    result = db.execute(stmt)
    return result.scalars().one_or_none()


def get_user_by_username(db: Session, username: str) -> User | None:
    stmt = (
        select(User)
        .where(User.username == username)
        .options(
            selectinload(User.role),
            selectinload(User.employee),
        )
    )
    result = db.execute(stmt)
    return result.scalars().one_or_none()
