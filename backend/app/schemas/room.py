from pydantic import BaseModel



class RoomCreate(BaseModel):
    number: str
    capacity: int
    description: str
    



    
class RoomResponse(BaseModel):
    id:int
    number: str
    capacity: int
    description: str
    
  