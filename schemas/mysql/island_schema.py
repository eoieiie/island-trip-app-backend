from pydantic import BaseModel

class IslandBase(BaseModel):
    tag_number: str
    name: str
    address: str
    coordinates: str
    photo: str
    info: str
    review_id: str
    activity_tag_numbers: str

class IslandCreate(IslandBase):
    pass

class Island(IslandBase):
    class Config:
        from_attributes = True
