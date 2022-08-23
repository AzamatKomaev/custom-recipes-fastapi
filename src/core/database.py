import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()

SQLALCHEMY_DATABASE_URL = 'postgresql+pg8000://{0}:{1}@localhost/{2}'.format(
    os.getenv('PGSQL_USER_NAME'),
    os.getenv('PGSQL_PASSWORD'),
    os.getenv('PGSQL_DB_NAME')
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# database = databases.Database(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
