from typing import List

from api.core import models
from api.schemas import city
from sqlalchemy.orm import Session


def get_city(db: Session, city_id: int) -> city.City:
    return db.query(models.City).filter(models.City.id == city_id).first()


def get_cities(db: Session, skip: int = 0, limit: int = 100) -> List[city.City]:
    return db.query(models.City).offset(skip).limit(limit).all()


def create_city(db: Session, city: city.CityRequest) -> city.City:
    db_city = models.City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city
