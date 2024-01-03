from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+pymysql://admin:123456@127.0.0.1:3306/db?charset=utf8"
engine = create_engine(DB_URL)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10))
    gender = Column(Integer, default=1, comment="1为男,2为女")

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

