from pydantic import BaseModel
from typing import List, Optional

class Post(BaseModel):
    island_tag_number: str
    place_tag_number: str
    user_id: int
    photos: Optional[List[bytes]] = None  # 이미지 데이터를 바이너리로 저장, 선택 사항
    keywords: List[str]
    rating: float
    review: str
