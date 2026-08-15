from pydantic import BaseModel


class SchoolClassCreate(BaseModel):
    class_group_id: int
    grade: int
    school_year: str
    home_teacher_id: int | None = None


class SchoolClassUpdate(BaseModel):
    class_group_id: int | None = None
    grade: int | None = None
    school_year: str | None = None
    home_teacher_id: int | None = None


class SchoolClassResponse(BaseModel):
    id: int
    class_group_id: int
    grade: int
    school_year: str
    class_group_name:str
    teacher_first_name: str | None
    teacher_last_name: str | None