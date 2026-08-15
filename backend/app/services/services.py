from sqlalchemy.orm import Session

from app.schemas.auth import UserUpdate
from app.models.user import User
from app.repositories.user_repository import (
    update_user,
    deactivate_user,
    get_employee,
    get_teacher,
    get_employees,
)


def update_user_info(
    db: Session,
    user: User,
    user_data: UserUpdate
):
    return update_user(db, user.id, user_data)


def archive_user(db: Session, user: User):
    return deactivate_user(db, user.id)


def get_teacher_info(db: Session, user: User):
    return get_teacher(db, user.id)


def get_stuff_info(db: Session, user: User):
    return get_employee(db, user.id)


def get_employees_info(db: Session):
    return get_employees(db)
