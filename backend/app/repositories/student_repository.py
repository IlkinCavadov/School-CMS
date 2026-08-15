from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentUpdate


def email_exists(db: Session, email: str) -> bool:
    stmt = select(Student).where(Student.email == email)
    result = db.execute(stmt)
    return result.scalars().one_or_none() is not None


def create(db: Session, student: Student) -> Student:
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_student_by_id(db: Session, student_id: int) -> Student | None:
    stmt = select(Student).where(Student.id == student_id)
    result = db.execute(stmt)
    return result.scalars().one_or_none()


def get_students(db: Session) -> list[Student]:
    stmt = (
        select(Student)
        .where(Student.end_date.is_(None))
        .order_by(Student.first_name, Student.last_name)
    )
    result = db.execute(stmt)
    return result.scalars().all()


def get_student_by_email(db: Session, email: str) -> Student | None:
    stmt = (
        select(Student)
        .where(Student.email == email)
    )
    result = db.execute(stmt)
    return result.scalars().one_or_none()


def update_student(
    db: Session,
    student_id: int,
    student_data: StudentUpdate
) -> Student | None:
    values = student_data.model_dump(exclude_unset=True)

    if values:
        stmt = (
            update(Student)
            .where(Student.id == student_id)
            .values(**values)
        )
        db.execute(stmt)
        db.commit()

    return get_student_by_id(db, student_id)


def delete_student(db: Session, student_id: int) -> Student:
    stmt = delete(Student).where(Student.id == student_id)
    db.execute(stmt)
    db.commit()
    return "Student deleted successfully"
