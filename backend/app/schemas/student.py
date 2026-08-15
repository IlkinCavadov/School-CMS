from pydantic import BaseModel, ConfigDict,EmailStr
from datetime import date



class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    start_date: date


class StudentUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None



    
class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    
  