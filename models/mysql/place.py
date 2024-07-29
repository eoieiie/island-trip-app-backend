from sqlalchemy import Column, String
from database.mysql import Base

class Place(Base):
    __tablename__ = "places"
    
    tag_number = Column(String(50), primary_key=True, index=True)  # 길이 지정
    activity_tag_number = Column(String(50), index=True)  
    name = Column(String(100), index=True)  
    address = Column(String(200))  
    coordinates = Column(String(100))  
    photo = Column(String(200))  
    naver_place_url = Column(String(200))  
