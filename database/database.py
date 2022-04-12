from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db

engine = create_engine(
    "sqlite:///db.sqlite3",
    connect_args={"check_same_thread": False}
)

meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()