from sqlalchemy.orm import Session

from app.models.student_history import StudentHistory
from app.schemas.student_history import StudentHistoryCreate
from app.repositories.student_history_repository import (
    create_student_history,
    get_student_history,
)


def create_student_history_info(
    db: Session,
    history_data: StudentHistoryCreate
) -> StudentHistory:
    history = StudentHistory(
        student_id=history_data.student_id,
        student_class_id=history_data.student_class_id,
        school_year=history_data.school_year,
    )

    return create_student_history(db, history)


def get_student_history_info(db: Session, student_id: int):
    return get_student_history(db, student_id)
