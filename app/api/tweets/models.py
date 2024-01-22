from typing import Optional

from pydantic import BaseModel


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