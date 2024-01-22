from typing import List, Optional

from fastapi import HTTPException, Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.api.users.models import User, UserResponse
from app.api.users.schema import UserORM
from app.db.init_db import get_db

router = APIRouter()


@router.post("/", response_model=UserResponse)
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


@router.get("/", response_model=List[User])
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
