from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base


class TweetORM(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, nullable=True)

    author = relationship("UserORM", back_populates="tweets")