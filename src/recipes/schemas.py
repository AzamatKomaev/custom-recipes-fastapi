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


class RecipeCreate(RecipeBase):
    pass


class RecipeSingle(RecipeBase):
    id: int
    is_active: bool
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class RecipeList(BaseModel):
    __root__: List[RecipeSingle]
