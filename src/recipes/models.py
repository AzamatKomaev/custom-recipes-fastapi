from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from core.utils import Column


Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
