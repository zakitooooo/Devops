from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
data_url = "postgresql://devops:devops123@localhost:5432/devops_db"

engine = create_engine(data_url)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

