from fastapi import APIRouter, HTTPException, status, File, UploadFile, Form
from typing import List, Optional
from models.mongodb.post import Post as MongoDBPost
from database.mongodb import post_collection
from schemas.mongodb.post_schema import individual_serial, list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
async def get_posts():
    """
    모든 포스트를 조회하여 반환하는 엔드포인트.
    """
    posts = list_serial(post_collection.find())
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(
    island_tag_number: str = Form(...),
    place_tag_number: str = Form(...),
    user_id: int = Form(...),
    keywords: str = Form(...),
    rating: float = Form(...),
    review: str = Form(...),
    photos: Optional[List[UploadFile]] = File(None)  # 선택 사항
):
    """
    포스트를 생성하는 엔드포인트.
    폼 데이터와 파일 업로드를 처리하여 MongoDB에 저장.
    """
    # 사진 파일 목록을 바이너리로 읽기 (선택 사항)
    photo_data_list = []
    if photos:
        for photo in photos:
            photo_data = await photo.read()
            photo_data_list.append(photo_data)

    # 포스트 데이터 생성
    post_data = {
        "island_tag_number": island_tag_number,
        "place_tag_number": place_tag_number,
        "user_id": user_id,
        "photos": photo_data_list,
        "keywords": keywords.split(","),
        "rating": rating,
        "review": review
    }

    # MongoDB에 데이터 삽입
    result = post_collection.insert_one(post_data)
    return {"id": str(result.inserted_id)}

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_post(id: str, post: MongoDBPost):
    """
    특정 포스트를 업데이트하는 엔드포인트.
    """
    if not post_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": post.dict()}):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post updated successfully"}

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_post(id: str):
    """
    특정 포스트를 삭제하는 엔드포인트.
    """
    if not post_collection.find_one_and_delete({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
