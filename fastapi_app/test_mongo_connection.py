from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# MongoDB Atlas 연결 확인
MONGO_DATABASE_URL = os.getenv('MONGO_DATABASE_URL')
client = MongoClient(MONGO_DATABASE_URL)
db = client.island

# 데이터베이스 이름과 컬렉션 이름 출력
print("Database names:", client.list_database_names())
print("Collections in 'island':", db.list_collection_names())
