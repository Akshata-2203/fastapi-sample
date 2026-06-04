from pydantic import BaseModel

# Schema for creating a new user (input)
class UserCreate(BaseModel):
    name: str
    age: int
    email: str

# Schema for returning user data (output)
class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True
