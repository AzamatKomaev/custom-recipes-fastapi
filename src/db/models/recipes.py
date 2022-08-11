from sqlalchemy import Column,  String, Integer
from db.config.database import Base


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
