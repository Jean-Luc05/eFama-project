# backend/schemas.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    phone_number: str
    password: str
    business_name: str
    province: str

class UserLogin(BaseModel):
    identifier: str
    password: str

class UserResponse(BaseModel):
    message: str
    user_id: str = None
    
class LoginResponse(BaseModel):
    message: str
    access_token: str = None
    user: dict = None