from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os
db_host = os.getenv("DB_HOST", "localhost")
data_url = f"postgresql://devops:devops123@{db_host}:5432/devops_db"
engine = create_engine(data_url)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

