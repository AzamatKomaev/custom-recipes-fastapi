import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

SQLALCHEMY_DATABASE_URL = 'postgresql+pg8000://{0}:{1}@localhost/{2}'.format(
    os.getenv('PGSQL_USER_NAME'),
    os.getenv('PGSQL_PASSWORD'),
    os.getenv('PGSQL_DB_NAME')
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

metadata = MetaData()


def run():
    print(metadata.tables)
    metadata.create_all(bind=engine)
