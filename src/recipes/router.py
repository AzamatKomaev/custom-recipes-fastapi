from typing import List

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from src.auth.jwt import get_current_user
from src.auth.schemas import TokenData
from src.core.database import get_db
from .schemas import RecipeCreate, RecipeSingle, RecipeFilter
from . import services


router = APIRouter()


@router.get('/', response_model=List[RecipeSingle], response_model_exclude={'cooking_steps'})
def get_all_recipes(request: Request, db: Session = Depends(get_db)):
    return services.get_recipe_list(db, {**request.query_params})


@router.get('/detail', response_model=RecipeSingle)
async def get_recipe(recipe_filter: RecipeFilter = Depends(), db: Session = Depends(get_db)):
    return await services.get_recipe_detail(db, recipe_filter.__dict__)


@router.post('/create', response_model=RecipeSingle, status_code=201)
async def create_recipe(
        item: RecipeCreate,
        db: Session = Depends(get_db),
        current_user: TokenData = Depends(get_current_user)
):
    return await services.create_recipe(db, item, current_user.id)
