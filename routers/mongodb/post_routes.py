from fastapi import APIRouter, Depends, HTTPException, status
from models.mongodb.post import Post as MongoDBPost
from database.mongodb import post_collection
from schemas.mongodb.post_schema import individual_serial, list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
async def get_posts():
    posts = list_serial(post_collection.find())
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(post: MongoDBPost):
    result = post_collection.insert_one(post.dict())
    return {"id": str(result.inserted_id)}

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_post(id: str, post: MongoDBPost):
    if not post_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": post.dict()}):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post updated successfully"}

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_post(id: str):
    if not post_collection.find_one_and_delete({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
