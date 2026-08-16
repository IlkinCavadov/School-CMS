from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.auth.jwt import get_current_user

from app.models.user import User

from app.schemas.subject import (
    SubjectCreate,
    SubjectResponse
)

from app.services.subject_services import (
    create_subject,
    get_subject,
    get_subjects,
)


router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


@router.post(
    "/",
    response_model=SubjectResponse
)
def create_subject(
    subject_data: SubjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to create a school class."
        )

    return create_subject(
        db,
        subject_data
    )


@router.get(
    "/",
    response_model=list[SubjectResponse]
)
def get_subjects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_subjects(db)


@router.get(
    "/{subject_id}",
    response_model=SubjectResponse
)
def get_subject_id(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    subject = get_subject(
        db,
        subject_id
    )

    if subject is None:
        raise HTTPException(
            status_code=404,
            detail="Room not found."
        )

    return subject

