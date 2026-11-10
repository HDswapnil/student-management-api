from pydantic import BaseModel, ConfigDict

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str

class StudentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    age: int
    grade: str
