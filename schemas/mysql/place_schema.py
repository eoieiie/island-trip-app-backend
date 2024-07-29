from pydantic import BaseModel

class PlaceBase(BaseModel):
    tag_number: str
    activity_tag_number: str
    name: str
    address: str
    coordinates: str
    photo: str
    naver_place_url: str

class PlaceCreate(PlaceBase):
    pass

class Place(PlaceBase):
    class Config:
        from_attributes = True
