from fastapi import APIRouter, HTTPException
from typing import List
from app.models.magazine_model import MagazineModel
from app.database import magazine_collection
from bson import ObjectId

router = APIRouter()

@router.post("/", response_description="Add new magazine", response_model=MagazineModel)
async def create_magazine(magazine: MagazineModel):
    magazine = await magazine_collection.insert_one(magazine.dict())
    created_magazine = await magazine_collection.find_one({"_id": magazine.inserted_id})
    return created_magazine

@router.get("/", response_description="List all magazines", response_model=List[MagazineModel])
async def list_magazines():
    magazines = await magazine_collection.find().to_list(1000)
    return magazines

@router.get("/{id}", response_description="Get a single magazine", response_model=MagazineModel)
async def show_magazine(id: str):
    if (magazine := await magazine_collection.find_one({"_id": ObjectId(id)})) is not None:
        return magazine
    raise HTTPException(status_code=404, detail=f"Magazine {id} not found")
