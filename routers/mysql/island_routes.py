from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.mysql import get_db
from models.mysql.island import Island as IslandModel
from schemas.mysql.island_schema import IslandCreate, Island

router = APIRouter()

@router.post("/", response_model=Island, status_code=status.HTTP_201_CREATED)
async def create_island(island: IslandCreate, db: Session = Depends(get_db)):
    db_island = IslandModel(**island.dict())
    db.add(db_island)
    db.commit()
    db.refresh(db_island)
    return db_island

@router.get("/{tag_number}", response_model=Island, status_code=status.HTTP_200_OK)
async def read_island(tag_number: str, db: Session = Depends(get_db)):
    island = db.query(Island).filter(IslandModel.tag_number == tag_number).first()
    if island is None:
        raise HTTPException(status_code=404, detail="Island not found")
    return island