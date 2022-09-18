from typing import List, Optional

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from auth.jwt import get_current_user
from auth.schemas import TokenData
from core.database import get_db
from .schemas import RecipeCreate, RecipeSingle
from . import services


router = APIRouter()


@router.get('/', response_model=List[RecipeSingle], response_model_exclude={'cooking_steps'})
def get_all_recipes(request: Request, db: Session = Depends(get_db)):
    return services.get_recipe_list(db, {**request.query_params})


@router.get('/{recipe_id}', response_model=RecipeSingle)
async def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return await services.get_recipe_by_id(db, recipe_id)


@router.post('/create', response_model=RecipeSingle, status_code=201)
async def create_recipe(
        item: RecipeCreate,
        db: Session = Depends(get_db),
        current_user: TokenData = Depends(get_current_user)
):
    return await services.create_recipe(db, item, current_user.id)
