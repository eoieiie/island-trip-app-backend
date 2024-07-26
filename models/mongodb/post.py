from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    island_tag_number: str
    place_tag_number: str
    author_id: int
    photos: List[str]
    keywords: List[str]
    rating: float
    review: str
