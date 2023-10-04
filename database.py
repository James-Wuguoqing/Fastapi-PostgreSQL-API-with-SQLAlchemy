from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEY_DATABASE_URL = "postgresql://wgq:wgq719100@localhost:5432/mydb"

Engine = create_engine(SQLALCHEY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()
