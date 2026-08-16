from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from app.models.subject import Subject



def create(db: Session, subject: Subject) -> Subject:
    db.add(subject)
    db.commit()
    db.refresh(subject)
    return subject


def get_subject_list(db:Session):
    stmt = select(Subject).order_by(Subject.name)
    result = db.execute(stmt)
    return result.scalars().all()

def get_one_subject(db:Session, subject_id:int) -> Subject | None:
    stmt = select(Subject).where(Subject.id == subject_id)
    result = db.execute(stmt)
    return result.scalars().one_or_none()
