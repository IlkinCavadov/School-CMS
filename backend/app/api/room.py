from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.auth.jwt import get_current_user

from app.models.user import User

from app.schemas.room import (
    RoomCreate,
    RoomResponse
)

from app.services.room_services import (
    create_room,
    get_room,
    get_rooms,
    delete_room_id
)


router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)


@router.post(
    "/",
    response_model=RoomResponse
)
def create_room(
    room_data: RoomCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to create a school class."
        )

    return create_room(
        db,
        room_data
    )


@router.get(
    "/",
    response_model=list[RoomResponse]
)
def get_school_classes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_rooms(db)


@router.get(
    "/{room_id}",
    response_model=RoomResponse
)
def get_school_class(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    room = get_room(
        db,
        room_id
    )

    if room is None:
        raise HTTPException(
            status_code=404,
            detail="Room not found."
        )

    return room


@router.delete(
    "/{room_id}",
    response_model=RoomResponse
)
def delete_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if current_user.role.name not in ["SuperAdmin", "Admin"]:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to update a school class."
        )

    return  delete_room_id(
        db,
        room_id
    )