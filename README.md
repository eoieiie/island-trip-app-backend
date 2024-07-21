fastapi_mongo_project/
├── app/
│   ├── __init__.py  # app 디렉토리를 패키지로 인식시키기 위해 사용
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── magazine_model.py  # 데이터를 정의하는 Pydantic 모델
│   │   └── user_model.py  # 데이터를 정의하는 Pydantic 모델
│   ├── database.py  # MongoDB 연결 설정을 정의하는 파일
│   └── routes/
│       ├── __init__.py
│       ├── magazine_routes.py  # 데이터를 관리하는 라우터를 정의
│       └── user_routes.py  # 데이터를 관리하는 라우터를 정의
└── requirements.txt


이런 느낌으로 구조를 짤거고, 
데이터베이스 모델이 생길때마다 models와 routes 부분에 정보가 추가될거야. 


app/database.py: MongoDB 연결 설정
app/models.py: Pydantic 모델을 정의
app/routes/magazine_routes.py: FastAPI 엔드포인트를 정의
app/main.py: FastAPI 애플리케이션을 설정하고 라우터를 포함시킴

새로운 데이터 모델 추가: 다른 데이터(댓글, 리뷰 등)를 추가하려면 새로운 Pydantic 모델을 app/models/ 디렉토리에 생성

새로운 라우터 추가: 새로운 데이터를 관리하려면 새로운 라우터를 app/routes/ 디렉토리에 생성

데이터베이스 컬렉션 추가: 새로운 데이터를 위한 컬렉션을 app/database.py 파일에 추가


관계형 DB 는 ORM 이라는 걸 사용. Mysql 은 관계형이라서 orm 이고 
몽고db는 관계형이 아니라서 odm을 사용. 

mysql 할 때 우리는 ORM 이라는 걸 사용해서 SQL 쿼리를 작성하지 않고 데이터베이스 작업을 수행할거임. 예를 들어볼게 

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

라는 객체지향 언어에서의 객체가 존재한다면

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

sql의 형식은 이렇다면 

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

위와 같은 형식으로 User 클래스와 데이터베이스의 users 테이블이 서로 매핑. 

몽고db는 odm을 사용하는데, 
