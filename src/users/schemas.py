from datetime import datetime
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class DisplayUser(UserBase):
    is_active: bool = True
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

