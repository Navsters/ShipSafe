from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#sqlite databse chosen for rapid development
SQLALCHEMY_DATABASE_URL = "sqlite:///./shipsafe.db"

#engine connects to our database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread":False},
)

#creates new isolated session objects
SessionLocal = sessionmaker(autocommit=False,autoflush=false,bind=engine)

#stores our ORM
Base=declarative_base()