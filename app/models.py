from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    goal = Column(String)
    duration = Column(Integer)
    frequency = Column(String)

def init_db():
    engine = create_engine('sqlite:///target.db')
    Base.metadata.create_all(engine)
    return engine