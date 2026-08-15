from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.auth.jwt import get_current_user

from app.models.user import User

from app.schemas.school_class import (
    SchoolClassCreate,
    SchoolClassUpdate,
    SchoolClassResponse,
)

from app.services.school_class_services import (
    create_school_class_info,
    get_school_class_info,
    get_school_classes_info,
    update_school_class_info,
)


router = APIRouter(
    prefix="/school-classes",
    tags=["School Classes"]
)


@router.post(
    "/",
    response_model=SchoolClassResponse
)
def create_school_class(
    class_data: SchoolClassCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to create a school class."
        )

    return create_school_class_info(
        db,
        class_data
    )


@router.get(
    "/",
    response_model=list[SchoolClassResponse]
)
def get_school_classes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_school_classes_info(db)


@router.get(
    "/{school_class_id}",
    response_model=SchoolClassResponse
)
def get_school_class(
    school_class_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    school_class = get_school_class_info(
        db,
        school_class_id
    )

    if school_class is None:
        raise HTTPException(
            status_code=404,
            detail="School class not found."
        )

    return school_class


@router.patch(
    "/{school_class_id}",
    response_model=SchoolClassResponse
)
def update_school_class(
    school_class_id: int,
    class_data: SchoolClassUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to update a school class."
        )

    school_class = update_school_class_info(
        db,
        school_class_id,
        class_data
    )

    if school_class is None:
        raise HTTPException(
            status_code=404,
            detail="School class not found."
        )

    return school_class