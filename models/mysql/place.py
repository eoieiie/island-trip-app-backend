from sqlalchemy import Column, String, Integer, Float
from database.mysql import Base
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql import func
import uuid

class Place(Base):
    __tablename__ = "places"
    
    uid = Column(CHAR(18), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    island_number = Column(Integer, index=True) # 섬 content id
    category = Column(String(200),index=True) # 카테고리(ex. 카페, 음식점, 액티비티)
    name = Column(String(100), index=True) # 상호명 
    address = Column(String(200)) # 도로명 주소 
    latitude = Column(Float) # 위도 좌표
    longitude = Column(Float) # 경도 좌표
    photo = Column(String(200)) # 이미지 URL
    naver_place = Column(String(1000)) # 네이버플레이스 URL