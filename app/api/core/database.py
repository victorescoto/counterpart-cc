import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = os.getenv("POSTGRES_USER", "postgres")
password = os.getenv("POSTGRES_PASSWORD", "")
server = os.getenv("POSTGRES_SERVER", "db")
db = os.getenv("POSTGRES_DB", "app")

engine = create_engine(f"postgresql://{user}:{password}@{server}/{db}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
