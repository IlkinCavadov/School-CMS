from pydantic import BaseModel


class StudentHistoryCreate(BaseModel):
    student_id: int
    student_class_id: int
    school_year: str


class StudentHistoryResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    grade: int
    class_group_name: str
    school_year: str

    class Config:
        from_attributes = True