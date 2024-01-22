from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """
    Model representing a user in the Twitter app.
    """
    username: str
    email: str
    full_name: Optional[str]


class UserResponse(BaseModel):
    """
    Model representing the response format for users.
    """
    customer: dict  # Change the type to strs
    message: str = "User created successfully"
