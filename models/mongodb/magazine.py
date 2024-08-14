from pydantic import BaseModel
from typing import List

class Magazine(BaseModel):
    island_tag_number: str
    thumbnail: bytes  # 이미지 데이터를 바이너리로 저장
    main_photo: bytes  # 이미지 데이터를 바이너리로 저장
    title: str
    photos: List[bytes]  # 이미지 데이터를 바이너리로 저장
    content: str
    related_place_tags: List[str]
