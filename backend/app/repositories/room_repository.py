from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from app.models.room import Room



def create(db: Session, room: Room) -> Room:
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


def get_rooms_list(db:Session):
    stmt = select(Room).order_by(Room.number)
    result = db.execute(stmt)
    return result.scalars().all()

def get_one_room(db:Session, room_id:int) -> Room | None:
    stmt = select(Room).where(Room.id == room_id)
    result = db.execute(stmt)
    return result.scalars().one_or_none()


def delete_room(db:Session, room_id:int):
    stmt = delete(Room).where(Room.id == room_id)
    db.execute(stmt)
    db.commit()
    return 'Room deleted successfully'