from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.auth.jwt import get_current_user

from app.models.user import User

from app.schemas.subject_assignment import (
    SubjectAssignmentCreate,
    SubjectAssignmentUpdate,
    SubjectAssignmentResponse,
)

from app.services.subject_assignment_services import (
    create_subject_assignment_info,
    get_subject_assignment_info,
    get_subject_assignments_info,
    update_subject_assignment_info,
    delete_subject_assignment_info,
)


router = APIRouter(
    prefix="/subject-assignments",
    tags=["Subject Assignments"]
)


@router.post(
    "/",
    response_model=SubjectAssignmentResponse
)
def create(
    assignment_data: SubjectAssignmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to create a subject assignment."
        )

    return create_subject_assignment_info(
        db,
        assignment_data
    )


@router.get(
    "/",
    response_model=list[SubjectAssignmentResponse]
)
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_subject_assignments_info(db)


@router.get(
    "/{subject_id}/{teacher_id}/{school_class_id}",
    response_model=SubjectAssignmentResponse
)
def get_one(
    subject_id: int,
    teacher_id: int,
    school_class_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    assignment = get_subject_assignment_info(
        db,
        subject_id,
        teacher_id,
        school_class_id,
    )

    if assignment is None:
        raise HTTPException(
            status_code=404,
            detail="Subject assignment not found."
        )

    return assignment


@router.patch(
    "/{subject_id}/{teacher_id}/{school_class_id}",
    response_model=SubjectAssignmentResponse
)
def update(
    subject_id: int,
    teacher_id: int,
    school_class_id: int,
    assignment_data: SubjectAssignmentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to update a subject assignment."
        )

    assignment = update_subject_assignment_info(
        db,
        subject_id,
        teacher_id,
        school_class_id,
        assignment_data,
    )

    if assignment is None:
        raise HTTPException(
            status_code=404,
            detail="Subject assignment not found."
        )

    return assignment


@router.delete(
    "/{subject_id}/{teacher_id}/{school_class_id}"
)
def delete(
    subject_id: int,
    teacher_id: int,
    school_class_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to delete a subject assignment."
        )

    deleted = delete_subject_assignment_info(
        db,
        subject_id,
        teacher_id,
        school_class_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Subject assignment not found."
        )

    return {
        "message": "Subject assignment deleted successfully."
    }