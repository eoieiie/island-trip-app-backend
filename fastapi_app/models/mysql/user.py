from sqlalchemy import Column, Integer, String
from database.mysql import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(100), index=True)  
    profile_photo = Column(String(200)) 
