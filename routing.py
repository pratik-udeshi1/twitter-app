from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from database import init_db, UserORM, TweetORM, SessionLocal
from models import User, Tweet, TweetResponse, UserResponse

app = FastAPI()

# Initialize the database
init_db()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=UserResponse)
async def create_user(user: User, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    if db.query(UserORM).filter(UserORM.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    user_dict = jsonable_encoder(user)
    db_user = UserORM(**user_dict)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    user_res = {
        'name': user.full_name,
        'email': user.email,
        'username': user.username,
    }

    user_response = UserResponse(customer=user_res, message="User created successfully")
    return user_response


@app.get("/users/", response_model=List[User])
async def get_users(email: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Retrieve users by email or get all users if email is not provided.
    """
    if email:
        # Retrieve users by email
        users = db.query(UserORM).filter(UserORM.email == email).all()
        if not users:
            raise HTTPException(status_code=404, detail="Users not found")
    else:
        # Retrieve all users
        users = db.query(UserORM).all()

    return users


@app.post("/tweets/", response_model=TweetResponse)
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


@app.get("/tweets/", response_model=List[Tweet])
async def get_tweets(db: Session = Depends(get_db)):
    """
    Retrieve all tweets.
    """
    return db.query(TweetORM).all()


@app.get("/tweets/{tweet_id}", response_model=Tweet)
async def read_tweet(tweet_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a tweet by tweet_id.
    """
    tweet = db.query(TweetORM).filter(TweetORM.id == tweet_id).first()
    if tweet:
        return tweet
    raise HTTPException(status_code=404, detail="Tweet not found")
