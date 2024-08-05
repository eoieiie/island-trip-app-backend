from pydantic import BaseModel

class PlaceBase(BaseModel):
    island_number: int  # 섬 content id
    category: str  # 카테고리(ex. 카페, 음식점, 액티비티)
    name: str  # 상호명 
    address: str  # 도로명 주소 
    latitude: float  # 위도 좌표
    longitude: float  # 경도 좌표
    photo: str  # 이미지 URL
    naver_place: str  # 가게 정보 (선택적)

class PlaceCreate(PlaceBase):
    pass

class Place(PlaceBase):
    uid: str  # UID 필드

    class Config:
        orm_mode = True