from fastapi import APIRouter, Depends, HTTPException, status
from models.mongodb.travel_list import TravelList as MongoDBTravelList
from database.mongodb import travel_list_collection
from schemas.mongodb.travel_list_schema import individual_serial, list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
async def get_travel_lists():
    travel_lists = list_serial(travel_list_collection.find())
    return travel_lists

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_travel_list(travel_list: MongoDBTravelList):
    result = travel_list_collection.insert_one(travel_list.dict())
    return {"id": str(result.inserted_id)}

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_travel_list(id: str, travel_list: MongoDBTravelList):
    if not travel_list_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": travel_list.dict()}):
        raise HTTPException(status_code=404, detail="Travel list not found")
    return {"message": "Travel list updated successfully"}

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_travel_list(id: str):
    if not travel_list_collection.find_one_and_delete({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail="Travel list not found")
    return {"message": "Travel list deleted successfully"}
