from app.db.database import init_db, SessionLocal

init_db()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
