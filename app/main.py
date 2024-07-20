from fastapi import FastAPI
from app.routes.magazine_routes import router as MagazineRouter

app = FastAPI()

app.include_router(MagazineRouter, tags=["magazines"], prefix="/magazines")
app.include_router(UserRouter, tags=["users"], prefix="/users")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the API!"}
