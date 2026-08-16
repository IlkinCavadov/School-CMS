from pydantic import BaseModel



class SubjectAssignmentCreate(BaseModel):
    subject_id: int
    teacher_id: int
    school_class_id:int
    


class SubjectAssignmentUpdate(BaseModel):
    subject_id: int | None=None
    teacher_id: int | None=None
    school_class_id:int | None=None
 
    
    
class SubjectAssignmentResponse(BaseModel):
    subject_id: int
    teacher_id: int
    school_class_id:int
    subject_name:str
    teacher_name: str
    school_class_name: str
    
  