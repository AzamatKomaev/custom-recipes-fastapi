from sqlalchemy import String, Boolean, DateTime, Integer, Column as DefaultColumn
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.core.utils import Column


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    is_active = DefaultColumn(Boolean, default=True, server_default="1")
    password = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    recipes = relationship('Recipe', backref='users')

    def __repr__(self):
        return f'<User(name={self.name} is_active={self.is_active})>'


users = User.__table__
