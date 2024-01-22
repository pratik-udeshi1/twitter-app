from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/twitter-app"

database = Database(DATABASE_URL)
Base = declarative_base()

engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
