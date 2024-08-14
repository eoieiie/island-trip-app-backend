from pydantic import BaseModel
from typing import List, Dict

class TravelList(BaseModel):
    #그냥 각 list 에 번호를 붙여서 일관적으로 관리해도 될 듯.?
    user_id: int
    travel_name: str
    island_tag_number: str
    start_date: str
    end_date: str
    daily_plans: List[Dict[str, str]]  # 하루 계획은 여러 개의 key-value 쌍을 포함할 수 있음

    
