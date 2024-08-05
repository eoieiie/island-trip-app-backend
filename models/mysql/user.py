from sqlalchemy import Column, Integer, String
from database.mysql import Base
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql import func
import uuid

class User(Base):
    __tablename__ = "users"
    
    uid = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(100), index=True)  
    profile_photo = Column(String(200)) 
