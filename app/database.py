from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os
database_url = os.getenv("DATABASE_URL")

if database_url is None:
    db_host = os.getenv("DB_HOST", "localhost")
    database_url = f"postgresql://devops:devops123@{db_host}:5432/devops_db"
engine = create_engine(database_url)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

