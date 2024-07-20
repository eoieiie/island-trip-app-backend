from fastapi import FastAPI
from app.routes.magazine_routes import router as MagazineRouter
from app.routes.user_routes import router as UserRouter


app = FastAPI()

#데이터베이스들의 router들을 추가해갈 공간 
app.include_router(MagazineRouter, tags=["magazines"], prefix="/magazines")
app.include_router(UserRouter, tags=["users"], prefix="/users")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the API!"}
