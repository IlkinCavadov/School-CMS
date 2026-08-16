from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from app.models.subject_assignment import SubjectAssignment
from app.models.subject import Subject
from app.models.teacher import Teacher
from app.models.user import User
from app.models.school_class import SchoolClass
from app.models.class_group import ClassGroup


def create_subject_assignment(
    db: Session,
    assignment: SubjectAssignment
) -> SubjectAssignment:

    db.add(assignment)
    db.commit()

    return assignment


def get_subject_assignment(
    db: Session,
    subject_id: int,
    teacher_id: int,
    school_class_id: int
):
    stmt = (
        select(
            SubjectAssignment.subject_id,
            SubjectAssignment.teacher_id,
            SubjectAssignment.school_class_id,

            Subject.name.label("subject_name"),

            User.first_name.label("teacher_first_name"),
            User.last_name.label("teacher_last_name"),

            SchoolClass.grade,
            ClassGroup.name.label("class_group_name"),
        )
        .join(
            Subject,
            Subject.id == SubjectAssignment.subject_id
        )
        .join(
            Teacher,
            Teacher.user_id == SubjectAssignment.teacher_id
        )
        .join(
            User,
            User.id == Teacher.user_id
        )
        .join(
            SchoolClass,
            SchoolClass.id == SubjectAssignment.school_class_id
        )
        .join(
            ClassGroup,
            ClassGroup.id == SchoolClass.class_group_id
        )
        .where(
            SubjectAssignment.subject_id == subject_id,
            SubjectAssignment.teacher_id == teacher_id,
            SubjectAssignment.school_class_id == school_class_id,
        )
    )

    result = db.execute(stmt)

    assignment = result.mappings().one_or_none()

    if assignment is None:
        return None

    return {
        **assignment,
        "teacher_name": (
            f"{assignment.teacher_first_name} "
            f"{assignment.teacher_last_name}"
        ),
        "school_class_name": (
            f"{assignment.grade}{assignment.class_group_name}"
        ),
    }


def get_subject_assignments(db: Session):

    stmt = (
        select(
            SubjectAssignment.subject_id,
            SubjectAssignment.teacher_id,
            SubjectAssignment.school_class_id,

            Subject.name.label("subject_name"),

            User.first_name.label("teacher_first_name"),
            User.last_name.label("teacher_last_name"),

            SchoolClass.grade,
            ClassGroup.name.label("class_group_name"),
        )
        .join(
            Subject,
            Subject.id == SubjectAssignment.subject_id
        )
        .join(
            Teacher,
            Teacher.user_id == SubjectAssignment.teacher_id
        )
        .join(
            User,
            User.id == Teacher.user_id
        )
        .join(
            SchoolClass,
            SchoolClass.id == SubjectAssignment.school_class_id
        )
        .join(
            ClassGroup,
            ClassGroup.id == SchoolClass.class_group_id
        )
        .order_by(
            SchoolClass.school_year,
            SchoolClass.grade,
            ClassGroup.name,
            Subject.name,
        )
    )

    result = db.execute(stmt)

    assignments = result.mappings().all()

    return [
        {
            **assignment,
            "teacher_name": (
                f"{assignment.teacher_first_name} "
                f"{assignment.teacher_last_name}"
            ),
            "school_class_name": (
                f"{assignment.grade}{assignment.class_group_name}"
            ),
        }
        for assignment in assignments
    ]


def update_subject_assignment(
    db: Session,
    old_subject_id: int,
    old_teacher_id: int,
    old_school_class_id: int,
    values: dict
):
    assignment = db.get(
        SubjectAssignment,
        (
            old_subject_id,
            old_teacher_id,
            old_school_class_id,
        )
    )

    if assignment is None:
        return None

    for key, value in values.items():
        setattr(assignment, key, value)

    db.commit()

    return get_subject_assignment(
        db,
        assignment.subject_id,
        assignment.teacher_id,
        assignment.school_class_id,
    )


def delete_subject_assignment(
    db: Session,
    subject_id: int,
    teacher_id: int,
    school_class_id: int
) -> bool:

    stmt = (
        delete(SubjectAssignment)
        .where(
            SubjectAssignment.subject_id == subject_id,
            SubjectAssignment.teacher_id == teacher_id,
            SubjectAssignment.school_class_id == school_class_id,
        )
    )

    result = db.execute(stmt)

    db.commit()

    return result.rowcount > 0