from sqlalchemy import Column,  String, Boolean, DateTime, Table, MetaData, Integer
from sqlalchemy.sql import func
from db.config.database import metadata, Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    is_active = Column(Boolean, default=True)
    password = Column(String(255)),
    created_at = Column(DateTime(timezone=True), server_default=func.now()),
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()),
