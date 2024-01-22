# app/main.py

from fastapi import FastAPI

from app.api.tweets.routing import router as tweets_router
from app.api.users.routing import router as users_router

app = FastAPI()

# Include routers from different routing modules
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(tweets_router, prefix="/tweets", tags=["tweets"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
