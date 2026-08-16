from app.models.subject import Subject
from app.schemas.subject import SubjectCreate, SubjectResponse
from app.repositories.subject_repository import (
    create,
    get_one_subject,
    get_subject_list
)
from sqlalchemy.orm import Session


def create_subject(db: Session, subject_data: SubjectCreate):
    subejct_data = Subject(
        name=subject_data.name,
        description=subject_data.description
    )

    return create(db, subject_data)


def get_subject(db: Session, subject_id: int):
    return get_one_subject(db, subject_id)


def get_subjects(db: Session):
    return get_subject_list(db)


