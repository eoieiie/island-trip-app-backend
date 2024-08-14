from fastapi import APIRouter, HTTPException, status, Form
from typing import List, Dict
import json
from models.mongodb.travel_list import TravelList as MongoDBTravelList
from database.mongodb import travel_list_collection
from schemas.mongodb.travel_list_schema import individual_serial, list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
async def get_travel_lists():
    """
    모든 여행 리스트를 조회하여 반환하는 엔드포인트.
    """
    travel_lists = list_serial(travel_list_collection.find())
    return travel_lists

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_travel_list(
    user_id: int = Form(...),
    travel_name: str = Form(...),
    island_tag_number: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    daily_plans: str = Form(...)  # daily_plans를 JSON 문자열로 받습니다.
):
    """
    여행 리스트를 생성하는 엔드포인트.
    """
    # daily_plans를 JSON 문자열에서 리스트로 변환
    try:
        daily_plans_list = json.loads(daily_plans)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="daily_plans must be a valid JSON string")

    # 여행 리스트 데이터 생성
    travel_list_data = {
        "user_id": user_id,
        "travel_name": travel_name,
        "island_tag_number": island_tag_number,
        "start_date": start_date,
        "end_date": end_date,
        "daily_plans": daily_plans_list
    }

    # MongoDB에 데이터 삽입
    result = travel_list_collection.insert_one(travel_list_data)
    return {"id": str(result.inserted_id)}

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_travel_list(
    id: str,
    user_id: int = Form(...),
    travel_name: str = Form(...),
    island_tag_number: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    daily_plans: str = Form(...)  # daily_plans를 JSON 문자열로 받습니다.
):
    """
    특정 여행 리스트를 업데이트하는 엔드포인트.
    """
    # daily_plans를 JSON 문자열에서 리스트로 변환
    try:
        daily_plans_list = json.loads(daily_plans)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="daily_plans must be a valid JSON string")

    # 업데이트할 여행 리스트 데이터
    travel_list_data = {
        "user_id": user_id,
        "travel_name": travel_name,
        "island_tag_number": island_tag_number,
        "start_date": start_date,
        "end_date": end_date,
        "daily_plans": daily_plans_list
    }

    # MongoDB에서 데이터 업데이트
    if not travel_list_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": travel_list_data}):
        raise HTTPException(status_code=404, detail="Travel list not found")
    return {"message": "Travel list updated successfully"}

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_travel_list(id: str):
    """
    특정 여행 리스트를 삭제하는 엔드포인트.
    """
    if not travel_list_collection.find_one_and_delete({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail="Travel list not found")
    return {"message": "Travel list deleted successfully"}
