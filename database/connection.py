import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.engine import URL

load_dotenv()

#Database cofiguration
Database_URL = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "3306")),
    database=os.getenv("DB_NAME")
)

#Create databse emgine
engine = create_engine(Database_URL, echo=True)

#Create session
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
    )

#Base class for SQLAlchemy models
Base = declarative_base()

#database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        