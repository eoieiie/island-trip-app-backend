# FastAPI Mongo Project Structure

fastapi_mongo_project/
├── app/
│ ├── init.py # app 디렉토리를 패키지로 인식시키기 위해 사용
│ ├── main.py
│ ├── models/
│ │ ├── init.py
│ │ ├── magazine_model.py # 데이터를 정의하는 Pydantic 모델
│ │ └── user_model.py # 데이터를 정의하는 Pydantic 모델
│ ├── database.py # MongoDB 연결 설정을 정의하는 파일
│ └── routes/
│ ├── init.py
│ ├── magazine_routes.py # 데이터를 관리하는 라우터를 정의
│ └── user_routes.py # 데이터를 관리하는 라우터를 정의
└── requirements.txt

## Project Structure Details

- `app/database.py`: MongoDB 연결 설정
- `app/models.py`: Pydantic 모델을 정의
- `app/routes/magazine_routes.py`: FastAPI 엔드포인트를 정의
- `app/main.py`: FastAPI 애플리케이션을 설정하고 라우터를 포함시킴

## Adding New Data Models

- **새로운 데이터 모델 추가**: 다른 데이터(댓글, 리뷰 등)를 추가하려면 새로운 Pydantic 모델을 `app/models/` 디렉토리에 생성
- **새로운 라우터 추가**: 새로운 데이터를 관리하려면 새로운 라우터를 `app/routes/` 디렉토리에 생성
- **데이터베이스 컬렉션 추가**: 새로운 데이터를 위한 컬렉션을 `app/database.py` 파일에 추가

## Notes on Database Usage

- **관계형 DB**: ORM을 사용하여 SQL 쿼리를 작성하지 않고 데이터베이스 작업을 수행 (예: MySQL)
- **비관계형 DB (MongoDB)**: ODM을 사용하여 데이터베이스 작업 수행
