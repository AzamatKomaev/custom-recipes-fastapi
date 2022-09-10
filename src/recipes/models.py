from sqlalchemy import Integer, String, Text, ARRAY, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from core.utils import Column


Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    description = Column(Text)
    cooking_steps = Column(ARRAY(Text))
    hashtags = Column(ARRAY(String))
    image = Column(String)
    is_active = Column(Boolean, default=True, server_default="1")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship('User', back_populates='recipes')

