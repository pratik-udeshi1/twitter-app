from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """
    Model representing a user in the Twitter app.
    """
    username: str
    email: str
    full_name: Optional[str]


class Tweet(BaseModel):
    """
    Model representing a tweet in the Twitter app.
    """
    content: str
    author_id: str
    created_at: Optional[str]  # You can use a more specific datetime type


class TweetResponse(BaseModel):
    """
    Model representing the response format for tweets.
    """
    tweet: Tweet
    message: str = "Tweet created successfully"


class UserResponse(BaseModel):
    """
    Model representing the response format for users.
    """
    customer: dict  # Change the type to strs
    message: str = "User created successfully"
