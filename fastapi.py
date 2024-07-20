from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI()

# MongoDB 연결 설정
client = AsyncIOMotorClient('mongodb+srv://<username>:<password>@<cluster-url>/magazineDB')
#이건 추후 추가 예정, .env 파일로 각자 해야 하나?

db = client.magazineDB

# Pydantic 모델, 필드는 아마 이렇게 할 듯 
class Magazine(BaseModel):
    tag_number: str
    thumbnail: str
    main_photo: str
    photos: list
    content: str
    related_place_tag_number: list

#엔드포인트들.


@app.post("/magazines/")
async def create_magazine(magazine: Magazine):
    result = await db.magazines.insert_one(magazine.dict())
    return {"id": str(result.inserted_id)}

#얘는 새로운 매거진 데이터 생성 후 몽고에 삽입함. 
#받는 데이터 형식은
'''
{
  "tag_number": "A1",
  "thumbnail": "thumbnail_url.jpg",
  "main_photo": "main_photo_url.jpg",
  "photos": ["photo1_url.jpg", "photo2_url.jpg"],
  "content": "This is a detailed article about A1 island.",
  "related_place_tag_number": ["P1", "P2"]
}
'''

#이걸 플러터로부터 받으려면 flutter에서 http 패키지 사용해야 함. 
#pubspec.yaml 파일에 http 패키지를 추가

#반환 데이터 형식은 삽입된 문서의 ID
'''
{
  "id": "60d21b4667d0d8992e610c85"
}
'''


@app.get("/magazines/")
async def get_magazines():
    magazines = await db.magazines.find().to_list(1000)
    return magazines

@app.get("/magazines/{id}")
async def get_magazine(id: str):
    magazine = await db.magazines.find_one({"_id": ObjectId(id)})
    if magazine is None:
        raise HTTPException(status_code=404, detail="Magazine not found")
    return magazine

#얘는 특정 ID의 데이터를 몽고에서 조회 후 반환함.만약 ID 없을 시 에러메시지 반환. 
'''
{
  "_id": "60d21b4667d0d8992e610c85",
  "tag_number": "A1",
  "thumbnail": "thumbnail_url.jpg",
  "main_photo": "main_photo_url.jpg",
  "photos": ["photo1_url.jpg", "photo2_url.jpg"],
  "content": "This is a detailed article about A1 island.",
  "related_place_tag_number": ["P1", "P2"]
}

''' 
