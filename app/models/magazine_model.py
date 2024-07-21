from pydantic import BaseModel, Field
from typing import List

class MagazineModel(BaseModel):
    tag_number: str
    thumbnail: str
    main_photo: str
    photos: List[str]
    content: str
    related_place_tag_number: List[str]

    class Config:
        schema_extra = {
            "example": {
                "tag_number": "A1",
                "thumbnail": "thumbnail_url.jpg",
                "main_photo": "main_photo_url.jpg",
                "photos": ["photo1_url.jpg", "photo2_url.jpg"],
                "content": "This is a detailed article about A1 island.",
                "related_place_tag_number": ["P1", "P2"]
            }
        }
#sqlalchemy 에서 맗하는 model은 db에 맵핑하기 위한 객체를 말하고 
#pydentic 에서 말하는 model은 어떤 값의 validation을 위해서 사용된다고 함. 
