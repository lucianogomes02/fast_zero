from typing import Optional

from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UpdateUser(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserPublic(BaseModel):
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserPublic]
