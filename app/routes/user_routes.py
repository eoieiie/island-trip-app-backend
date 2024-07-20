from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user_model import UserModel
from app.database import user_collection
from bson import ObjectId

router = APIRouter()

@router.post("/", response_description="Add new user", response_model=UserModel)
async def create_user(user: UserModel):
    user = await user_collection.insert_one(user.dict())
    created_user = await user_collection.find_one({"_id": user.inserted_id})
    return created_user

@router.get("/", response_description="List all users", response_model=List[UserModel])
async def list_users():
    users = await user_collection.find().to_list(1000)
    return users

@router.get("/{id}", response_description="Get a single user", response_model=UserModel)
async def show_user(id: str):
    if (user := await user_collection.find_one({"_id": ObjectId(id)})) is not None:
        return user
    raise HTTPException(status_code=404, detail=f"User {id} not found")
