# migrate_db.py

from database import Base, engine

# Bind the engine to the metadata of the Base class
Base.metadata.create_all(bind=engine)
