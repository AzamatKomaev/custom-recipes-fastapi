from pydantic import BaseModel


class RecipeBase(BaseModel):
    name: str


class RecipeCreate(RecipeBase):
    name: str


class RecipeSingle(RecipeBase):
    id: int

    class Config:
        orm_mode = True
