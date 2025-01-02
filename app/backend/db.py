from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String


# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


engine = create_engine("sqlite:///taskmanager.db", echo=True)
SessionLocal = sessionmaker(bind=engine)



class Base(DeclarativeBase):
    pass

