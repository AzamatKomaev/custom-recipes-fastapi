from sqlalchemy import Column,  String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
