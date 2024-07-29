from pydantic import BaseModel
from typing import List, Dict

class TravelList(BaseModel):
    user_id: int
    travel_name: str
    island_tag_number: str
    start_date: str
    end_date: str
    daily_plans: List[Dict[str, str]]
