from fastapi import APIRouter, HTTPException, status, File, UploadFile, Form
from typing import List, Optional
from models.mongodb.magazine import Magazine as MongoDBMagazine
from database.mongodb import magazine_collection
from schemas.mongodb.magazine_schema import individual_serial, list_serial
from bson import ObjectId
import io

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
async def get_magazines():
    """
    모든 매거진을 조회하여 반환하는 엔드포인트.
    """
    magazines = list_serial(magazine_collection.find())
    return magazines

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_magazine(
    tag_number: str = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    related_place_tags: str = Form(...),
    thumbnail: UploadFile = File(...),  # 필수 필드
    main_photo: Optional[UploadFile] = File(None),  # 선택 필드
    photos: List[UploadFile] = File(...)  # 필수 필드
):
    """
    매거진을 생성하는 엔드포인트.
    폼 데이터와 파일 업로드를 처리하여 MongoDB에 저장.
    """
    # 썸네일 파일을 바이너리로 읽기
    thumbnail_data = await thumbnail.read()

    # 메인 사진 파일을 바이너리로 읽기 (선택 사항)
    main_photo_data = await main_photo.read() if main_photo else None # none 붙였으니까 그거에 대한 오류 방지

    # 사진 파일 목록을 바이너리로 읽기
    photo_data_list = []
    for photo in photos:
        photo_data = await photo.read()
        photo_data_list.append(photo_data)

    # 매거진 데이터 생성
    magazine_data = {
        "tag_number": tag_number,
        "thumbnail": thumbnail_data,
        "main_photo": main_photo_data,
        "title": title,
        "photos": photo_data_list,
        "content": content,
        "related_place_tags": related_place_tags.split(",")
    }

    # MongoDB에 데이터 삽입
    result = magazine_collection.insert_one(magazine_data)
    return {"id": str(result.inserted_id)}

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_magazine(id: str, magazine: MongoDBMagazine):
    """
    특정 매거진을 업데이트하는 엔드포인트.
    """
    if not magazine_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": magazine.dict()}):
        raise HTTPException(status_code=404, detail="Magazine not found")
    return {"message": "Magazine updated successfully"}

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_magazine(id: str):
    """
    특정 매거진을 삭제하는 엔드포인트.
    """
    if not magazine_collection.find_one_and_delete({"_id": ObjectId(id)}):
        raise HTTPException(status_code=404, detail="Magazine not found")
    return {"message": "Magazine deleted successfully"}
