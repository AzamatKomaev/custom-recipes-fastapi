from datetime import datetime
from typing import List
from pydantic import BaseModel


class RecipeBase(BaseModel):
    name: str
    type: str
    description: str
    cooking_steps: List[str]
    hashtags: List[str]
    image: str
    is_active: bool
    user_id: int


class RecipeCreate(RecipeBase):
    pass


class RecipeSingle(RecipeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
