from fastapi import HTTPException, status
from sqlalchemy import any_, desc
from sqlalchemy.orm import Session

from . import schemas
from . import models


def get_recipe_list(db: Session, query: dict):
    """Get recipe list and return recipes list."""
    filter_list = []

    name = query.get('name')
    hashtag = query.get('hashtag')
    recipe_type = query.get('type')
    author_id = query.get('user_id')
    order_by = query.get('order_by', 'created_at')
    ordering_list = ['name', 'created_at']

    if order_by not in ordering_list:
        raise HTTPException(status_code=422, detail='Invalid order_by value.')

    if name is not None:
        filter_list.append(models.Recipe.name.contains(name))

    if hashtag is not None:
        filter_list.append('#' + hashtag == any_(models.Recipe.hashtags))

    if recipe_type is not None:
        filter_list.append(models.Recipe.type.like(recipe_type))

    if author_id is not None and author_id.isdigit():
        filter_list.append(models.Recipe.user_id == int(author_id))

    recipes = db.query(models.Recipe).filter(*filter_list).order_by(desc(order_by)).all()
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
