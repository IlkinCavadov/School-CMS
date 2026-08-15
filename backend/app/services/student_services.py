from app.models.student import Student
from app.schemas.student import StudentUpdate, StudentCreate
from app.repositories.student_repository import (
    create,
    get_student_by_id,
    update_student,
    delete_student,
    email_exists,
    get_student_by_email,
    get_students,
)
from app.repositories.role_repository import get_role_by_name
from sqlalchemy.orm import Session


def create_student(db: Session, student_data: StudentCreate):
    email_check = email_exists(db, student_data.email)
    role = get_role_by_name(db, "User")

    if role is None:
        raise ValueError("User role does not exist. Run seed_roles.py first.")

    if email_check:
        raise ValueError("Email already exists.")

    student = Student(
        first_name=student_data.first_name,
        last_name=student_data.last_name,
        emai=student_data.email,
        start_date=student_data.start_date,
    )

    return create(db, student)


def update_student_info(
    db: Session,
    student: Student,
    student_data: StudentUpdate
):
    return update_student(db, student.id, student_data)


def get_student_id(db: Session, student: Student):
    return get_student_by_id(db, student.id)


def get_student_info(db: Session, email: str):
    return get_student_by_email(db, email)


def get_students_info(db: Session):
    return get_students(db)


def delete_student_id(db: Session, student_id: int):
    return delete_student(db, student_id)
