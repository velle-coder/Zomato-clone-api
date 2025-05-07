from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
import schemas, models
from database import SessionLocal

router = APIRouter(prefix="/dishes", tags=["Dishes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/dishes", response_model=schemas.DishOut)
def create_dish(dish: schemas.DishCreate, db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).filter_by(id=dish.restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail= "restaurant not found")

    new_dish = models.Dish(**dish.dict())
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish


@router.get("/", response_model=list[schemas.DishOut])
def list_dishes(db:Session= Depends(get_db)):
    return db.query(models.Dish).all()






