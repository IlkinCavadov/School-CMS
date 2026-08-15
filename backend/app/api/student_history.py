from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.auth.jwt import get_current_user

from app.models.user import User

from app.schemas.student_history import StudentHistoryResponse

from app.services.student_history_services import (
    get_student_history_info,
)


router = APIRouter(
    prefix="/students",
    tags=["Student History"]
)


@router.get(
    "/{student_id}/history",
    response_model=list[StudentHistoryResponse]
)
def get_history(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_student_history_info(
        db,
        student_id
    )