from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str
