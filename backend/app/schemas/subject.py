from pydantic import BaseModel



class SubjectCreate(BaseModel):
    name: str
    description: str
    



    
class SubjectResponse(BaseModel):
    id:int
    name: str
    description: str
    
  