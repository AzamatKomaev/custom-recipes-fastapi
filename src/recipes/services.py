from fastapi import HTTPException, status
from sqlalchemy import any_
from sqlalchemy.orm import Session

from . import schemas
from . import models


def get_recipe_list(db: Session, filter_params: dict):
    """Get recipe list and return recipes list."""
    filter_list = []

    name = filter_params.get('name')
    hashtag = filter_params.get('hashtag')

    if name is not None:
        filter_list.append(models.Recipe.name.like(name))

    if hashtag is not None:
        filter_list.append('#' + hashtag == any_(models.Recipe.hashtags))

    recipes = db.query(models.Recipe).filter(*filter_list).all()
    return recipes


async def get_recipe_by_id(db: Session, recipe_id: int):
    recipe = db.query(models.Recipe).get(recipe_id)
    if not recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !")
    return schemas.RecipeSingle(**recipe.__dict__)


async def create_recipe(db: Session, item: schemas.RecipeCreate, user_id: int) -> models.Recipe:
    """Create recipe and return Recipe object."""
    recipe = models.Recipe(**item.dict(), user_id=user_id)
    db.add(recipe)
    db.flush()
    db.commit()
    db.refresh(recipe)
    return recipe
