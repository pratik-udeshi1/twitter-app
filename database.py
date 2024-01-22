from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/twitter-app"

database = Database(DATABASE_URL)
Base = declarative_base()

engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


# Define ORM models
class UserORM(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    full_name = Column(String, index=True)

    tweets = relationship("TweetORM", back_populates="author")


class TweetORM(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, nullable=True)

    author = relationship("UserORM", back_populates="tweets")
