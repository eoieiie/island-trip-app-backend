from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import certifi

# MongoDB 연결 설정
MONGO_DETAILS = "mongodb+srv://eoieiie:<0315>@test.9yvnmpr.mongodb.net/?retryWrites=true&w=majority&appName=test"

client = AsyncIOMotorClient(MONGO_DETAILS, tlsCAFile=certifi.where())
database = client.magazineDB


magazine_collection = database.get_collection("magazines")
user_collection = database.get_collection("users")
