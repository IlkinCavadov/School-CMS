from sqlalchemy.orm import Session

from app.models.school_class import SchoolClass
from app.schemas.school_class import (
    SchoolClassCreate,
    SchoolClassUpdate,
)
from app.repositories.school_class_repository import (
    create_school_class,
    get_school_class_by_id,
    get_school_classes,
    update_school_class,
)


def create_school_class_info(
    db: Session,
    class_data: SchoolClassCreate
) -> SchoolClass:
    school_class = SchoolClass(
        class_group_id=class_data.class_group_id,
        grade=class_data.grade,
        school_year=class_data.school_year,
        home_teacher_id=class_data.home_teacher_id,
    )
    return create_school_class(db, school_class)


def get_school_class_info(
    db: Session,
    school_class_id: int
) -> SchoolClass | None:
    return get_school_class_by_id(db, school_class_id)


def get_school_classes_info(db: Session) -> list[SchoolClass]:
    return get_school_classes(db)


def update_school_class_info(
    db: Session,
    school_class_id: int,
    class_data: SchoolClassUpdate
) -> SchoolClass | None:
    values = class_data.model_dump(exclude_unset=True)
    return update_school_class(db, school_class_id, values)
