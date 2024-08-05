from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.mysql import get_db
from models.mysql.place import Place as PlaceModel
from schemas.mysql.place_schema import PlaceCreate, Place

router = APIRouter()

@router.post("/", response_model=Place, status_code=status.HTTP_201_CREATED)
async def create_place(place: PlaceCreate, db: Session = Depends(get_db)):
    db_place = PlaceModel(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

# uid로 호출
@router.get("/{uid}", response_model=Place, status_code=status.HTTP_200_OK)
async def read_place(uid: str, db: Session = Depends(get_db)):
    place = db.query(PlaceModel).filter(PlaceModel.uid == uid).first()
    if place is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return place