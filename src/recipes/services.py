from sqlalchemy.orm import Session
from .schemas import RecipeCreate, RecipeList
from . import models


async def get_recipe_list(db: Session) -> RecipeList:
    """Get recipe list and return recipes list."""
    recipes = db.query(models.Recipe).all()
    return recipes


async def create_recipe(db: Session, item: RecipeCreate, user_id: int) -> models.Recipe:
    """Create recipe and return Recipe object."""
    print(item.dict())
    recipe = models.Recipe(**item.dict(), user_id=user_id)
    db.add(recipe)
    db.flush()
    db.commit()
    db.refresh(recipe)
    return recipe
