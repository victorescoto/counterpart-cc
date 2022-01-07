from typing import List

from api.core.dependencies import get_db
from api.crud import city as city_crud
from api.schemas.city import City, CityRequest
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

router = APIRouter()


@router.get("/city", response_model=List[City], tags=["city"])
def list_cities(db: Session = Depends(get_db)):
    cities = city_crud.get_cities(db)
    return cities


@router.post("/city", response_model=City, tags=["city"])
def create_city(request_params: CityRequest, db: Session = Depends(get_db)):
    city = city_crud.create_city(db, request_params)
    return city
