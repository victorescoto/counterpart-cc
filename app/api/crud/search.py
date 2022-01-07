from typing import List

from api.core import models
from api.schemas import search
from sqlalchemy.orm import Session


def get_searches(db: Session, skip: int = 0, limit: int = 100) -> List[search.Search]:
    return db.query(models.Search).offset(skip).limit(limit).all()


def create_search(db: Session, search: search.SearchDBCreate) -> search.Search:
    db_search = models.Search(**search.dict())
    db.add(db_search)
    db.commit()
    db.refresh(db_search)
    return db_search
