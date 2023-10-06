from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

#load_dotenv()
# SQLALCHEY_DATABASE_URL = os.getenv('DATABASE_URL')

# engine = create_engine('SQLALCHEY_DATABASE_URL')
engine=create_engine("postgresql://ezcc:ezcc@localhost:5432/ezcc_db")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
