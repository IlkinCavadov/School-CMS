from sqlalchemy.orm import Session

from app.models.subject_assignment import SubjectAssignment
from app.schemas.subject_assignment import (
    SubjectAssignmentCreate,
    SubjectAssignmentUpdate,
)

from app.repositories.subject_assignment_repository import (
    create_subject_assignment,
    get_subject_assignment,
    get_subject_assignments,
    update_subject_assignment,
    delete_subject_assignment,
)


def create_subject_assignment_info(
    db: Session,
    assignment_data: SubjectAssignmentCreate
):

    assignment = SubjectAssignment(
        subject_id=assignment_data.subject_id,
        teacher_id=assignment_data.teacher_id,
        school_class_id=assignment_data.school_class_id,
    )

    return create_subject_assignment(
        db,
        assignment
    )


def get_subject_assignment_info(
    db: Session,
    subject_id: int,
    teacher_id: int,
    school_class_id: int
):

    return get_subject_assignment(
        db,
        subject_id,
        teacher_id,
        school_class_id,
    )


def get_subject_assignments_info(db: Session):

    return get_subject_assignments(db)


def update_subject_assignment_info(
    db: Session,
    subject_id: int,
    teacher_id: int,
    school_class_id: int,
    assignment_data: SubjectAssignmentUpdate,
):

    values = assignment_data.model_dump(
        exclude_unset=True,
        exclude_none=True,
    )

    return update_subject_assignment(
        db,
        subject_id,
        teacher_id,
        school_class_id,
        values,
    )


def delete_subject_assignment_info(
    db: Session,
    subject_id: int,
    teacher_id: int,
    school_class_id: int,
):

    return delete_subject_assignment(
        db,
        subject_id,
        teacher_id,
        school_class_id,
    )