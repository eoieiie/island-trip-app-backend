from sqlalchemy import Column, String
from database.mysql import Base

class Island(Base):
    __tablename__ = "islands"
    
    tag_number = Column(String(50), primary_key=True, index=True) 
    name = Column(String(100), index=True)  
    address = Column(String(200))  
    coordinates = Column(String(100))  
    photo = Column(String(200))  
    info = Column(String(1000))  
    review_id = Column(String(50))  
    activity_tag_numbers = Column(String(200))  