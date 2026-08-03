from pydantic import BaseModel

class StudentCreate(BaseModel):
    name:str
    department:str
    semester:int
    math:int
    science:int
    english:int
    attendance:float

class StudentResponse(StudentCreate):
    id:int

    class Config:
        from_attributes=True