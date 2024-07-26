from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

MONGO_DATABASE_URL = os.getenv('MONGO_DATABASE_URL')


client = MongoClient(MONGO_DATABASE_URL)


db = client.island
magazine_collection = db["magazine_collection"]
post_collection = db["post_collection"]
travel_list_collection = db["travel_list_collection"]

def get_mongo_db():
    return db
