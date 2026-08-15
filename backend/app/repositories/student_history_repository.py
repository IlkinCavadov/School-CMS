from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.student_history import StudentHistory
from app.models.student import Student
from app.models.school_class import SchoolClass
from app.models.class_group import ClassGroup


def create_student_history(
    db: Session,
    history: StudentHistory
) -> StudentHistory:
    db.add(history)
    db.commit()
    db.refresh(history)
    return history


def get_student_history(db: Session, student_id: int):
    stmt = (
        select(
            StudentHistory.id,
            Student.first_name,
            Student.last_name,
            SchoolClass.grade,
            ClassGroup.name.label("class_group_name"),
            StudentHistory.school_year,
        )
        .join(Student, Student.id == StudentHistory.student_id)
        .join(
            SchoolClass,
            SchoolClass.id == StudentHistory.student_class_id
        )
        .join(
            ClassGroup,
            ClassGroup.id == SchoolClass.class_group_id
        )
        .where(StudentHistory.student_id == student_id)
        .order_by(StudentHistory.school_year)
    )

    result = db.execute(stmt)
    return result.mappings().all()
