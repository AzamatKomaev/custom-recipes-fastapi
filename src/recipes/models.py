from sqlalchemy import Integer, String, Text, ARRAY, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from core.database import Base
from core.utils import Column


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

    user_id = Column(Integer, ForeignKey('users.id'))
