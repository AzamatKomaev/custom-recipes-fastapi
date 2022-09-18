from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserSingle(UserBase):
    id: int
    is_active: bool
    recipes_count: int = 0
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserList(BaseModel):
    __root__: List[UserSingle]
