from sqlalchemy.orm import Session
from core.database import get_db
from .models import Recipe
from .schemas import RecipeCreate, RecipeSingle


recipes = Recipe.__table__


async def get_recipe_list(db_session: Session):
    return await db_session.query()


async def create_recipe(item: RecipeCreate):
    query = recipes.insert().values(**item.dict())
    recipe_id = await database.execute(query)
    return RecipeSingle(**item.dict(), id=recipe_id)