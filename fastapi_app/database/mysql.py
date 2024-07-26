from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# 이걸로  url 암호화. 상위 디렉터리에 .env 파일 생성 후 그 안에 MYSQL_DATABASE_URL = url주소 넣어두면 됨. github에 push 할 때는 .gitignore 안에 .env 추가해주기. 
load_dotenv()

# Get MySQL database URL from environment variables
DATABASE_URL = os.getenv('MYSQL_DATABASE_URL')

# Create engine
engine = create_engine(DATABASE_URL)

# Create session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
