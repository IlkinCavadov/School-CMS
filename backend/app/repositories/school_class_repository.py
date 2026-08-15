from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.school_class import SchoolClass
from app.models.class_group import ClassGroup
from app.models.teacher import Teacher
from app.models.user import User


def create_school_class(
    db: Session,
    school_class: SchoolClass
) -> SchoolClass:

    db.add(school_class)
    db.commit()
    db.refresh(school_class)

    return school_class


def get_school_class_by_id(
    db: Session,
    school_class_id: int
):
    stmt = (
        select(
            SchoolClass.id,
            SchoolClass.class_group_id,
            SchoolClass.grade,
            SchoolClass.school_year,
            ClassGroup.name.label("class_group_name"),
            User.first_name.label("teacher_first_name"),
            User.last_name.label("teacher_last_name"),
        )
        .join(
            ClassGroup,
            ClassGroup.id == SchoolClass.class_group_id
        )
        .outerjoin(
            Teacher,
            Teacher.user_id == SchoolClass.home_teacher_id
        )
        .outerjoin(
            User,
            User.id == Teacher.user_id
        )
        .where(SchoolClass.id == school_class_id)
    )

    result = db.execute(stmt)

    return result.mappings().one_or_none()


def get_school_classes(db: Session):
    stmt = (
        select(
            SchoolClass.id,
            SchoolClass.class_group_id,
            SchoolClass.grade,
            SchoolClass.school_year,
            ClassGroup.name.label("class_group_name"),
            User.first_name.label("teacher_first_name"),
            User.last_name.label("teacher_last_name"),
        )
        .join(
            ClassGroup,
            ClassGroup.id == SchoolClass.class_group_id
        )
        .outerjoin(
            Teacher,
            Teacher.user_id == SchoolClass.home_teacher_id
        )
        .outerjoin(
            User,
            User.id == Teacher.user_id
        )
        .order_by(
            SchoolClass.school_year,
            SchoolClass.grade,
            ClassGroup.name
        )
    )

    result = db.execute(stmt)

    return result.mappings().all()


def update_school_class(
    db: Session,
    school_class_id: int,
    values: dict
):
    school_class = (
        db.execute(
            select(SchoolClass)
            .where(SchoolClass.id == school_class_id)
        )
        .scalars()
        .one_or_none()
    )

    if school_class is None:
        return None

    for key, value in values.items():
        setattr(school_class, key, value)

    db.commit()

    return get_school_class_by_id(db, school_class_id)