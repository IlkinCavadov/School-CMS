from app.models.room import Room
from app.schemas.room import RoomCreate, RoomResponse
from app.repositories.room_repository import (
    create,
    get_one_room,
    get_rooms_list,
    delete_room
)
from sqlalchemy.orm import Session


def create_room(db: Session, room_data: RoomCreate):
    room = Room(
        number=room_data.number,
        capacity=room_data.capacity,
        description=room_data.description
    )

    return create(db, room)


def get_room(db: Session, room_id: int):
    return get_one_room(db, room_id)


def get_rooms(db: Session):
    return get_rooms_list(db)


def delete_room_id(db: Session, room_id: int):
    return delete_room(db, room_id)
