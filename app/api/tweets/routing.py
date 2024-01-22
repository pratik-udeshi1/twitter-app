from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.api.tweets.models import TweetResponse, Tweet
from app.api.tweets.schema import TweetORM
from app.api.users.schema import UserORM
from app.db.init_db import get_db

router = APIRouter()


@router.post("/", response_model=TweetResponse)
async def create_tweet(tweet: Tweet, db: Session = Depends(get_db)):
    """
    Create a new tweet.
    """
    user = db.query(UserORM).filter(UserORM.id == tweet.author_id).first()

    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")

    db_tweet = TweetORM(content=tweet.content, author=user)
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return {"tweet": tweet, "message": "Tweet created successfully"}


@router.get("/", response_model=List[Tweet])
async def get_tweets(db: Session = Depends(get_db)):
    """
    Retrieve all tweets.
    """
    return db.query(TweetORM).all()


@router.get("{tweet_id}", response_model=Tweet)
async def read_tweet(tweet_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a tweet by tweet_id.
    """
    tweet = db.query(TweetORM).filter(TweetORM.id == tweet_id).first()
    if tweet:
        return tweet
    raise HTTPException(status_code=404, detail="Tweet not found")
