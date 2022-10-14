from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field


class RecipeBase(BaseModel):
    name: str
    type: str
    description: str
    cooking_steps: List[str]
    hashtags: List[str]
    image: Optional[str] = None


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


class RecipeFilter(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
