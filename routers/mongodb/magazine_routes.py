from fastapi import APIRouter, Depends, HTTPException, status
from models.mongodb.magazine import Magazine as MongoDBMagazine
from database.mongodb import magazine_collection
from schemas.mongodb.magazine_schema import individual_serial, list_serial
from bson import ObjectId

router = APIRouter()

# 엔드포인트 / 이렇게 해도 될까?
@router.get("/", status_code=status.HTTP_200_OK)
async def get_magazines():
    magazines = list_serial(magazine_collection.find())
    return magazines

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_magazine(magazine: MongoDBMagazine):
    result = magazine_collection.insert_one(magazine.dict())
    return {"id": str(result.inserted_id)}

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_magazine(id: str, magazine: MongoDBMagazine):
    if not magazine_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": magazine.dict()}):
        raise HTTPException(status_code=404, detail="Magazine not found")
    return {"message": "Magazine updated successfully"}

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_magazine(id: str):
    if not magazine_collection.find_one_and_delete({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail="Magazine not found")
    return {"message": "Magazine deleted successfully"}