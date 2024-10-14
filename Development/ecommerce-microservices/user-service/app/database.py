import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Get the database URL from the environment variable or set a default
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db-service:5432/ecommerce")

# Create the database engine without connect_args for PostgreSQL
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get the session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
