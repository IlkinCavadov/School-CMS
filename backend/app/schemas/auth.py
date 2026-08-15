from pydantic import BaseModel, ConfigDict,EmailStr
from datetime import date



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
    

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    password: str
    employee_type: str
    hire_date: date


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    username: str | None = None



    
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    employee_type: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
  