from pydantic import BaseModel
from typing import List

class Magazine(BaseModel):
    tag_number: str
    thumbnail: str
    main_photo: str
    title: str
    photos: List[str]
    content: str
    related_place_tags: List[str]
