from fastapi import FastAPI, HTTPException
from database.mysql import Base, engine
from routers.mysql import island_routes, place_routes, user_routes
from routers.mongodb import magazine_routes, travel_list_routes, post_routes

app = FastAPI()

# MySQL 데이터베이스 초기화
Base.metadata.create_all(bind=engine)

# MySQL 라우터 추가
app.include_router(island_routes.router, prefix="/mysql/islands", tags=["islands"])
app.include_router(place_routes.router, prefix="/mysql/places", tags=["places"])
app.include_router(user_routes.router, prefix="/mysql/users", tags=["users"])

# MongoDB 라우터 추가
app.include_router(magazine_routes.router, prefix="/mongodb/magazines", tags=["magazines"])
app.include_router(travel_list_routes.router, prefix="/mongodb/travel_lists", tags=["travel_lists"])
app.include_router(post_routes.router, prefix="/mongodb/posts", tags=["posts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
