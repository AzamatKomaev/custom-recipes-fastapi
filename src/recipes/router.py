from fastapi import APIRouter
from .schemas import RecipeSingle, RecipeCreate
from . import services

router = APIRouter()


@router.get('/')
async def get_recipes():
    return await services.get_recipe_list()


@router.post('/create', status_code=201)
async def create_recipe(item: RecipeCreate):
    return await services.create_recipe(item)
