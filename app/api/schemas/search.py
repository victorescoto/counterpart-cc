from datetime import date, timedelta
from typing import Union

from pydantic import BaseModel, Field


class EarthquakeDistance(BaseModel):
    title: str
    time: int
    distance: float


class SearchRequest(BaseModel):
    city_id: int
    start_date: date = Field(..., example=date.today() - timedelta(days=30))
    end_date: date = Field(..., example=date.today())


class SearchResponse(BaseModel):
    city_name: str = Field(..., example="Los Angeles, CA")
    title: str = Field(..., example="M 5.3 - off the coast of Oregon")
    time: int = Field(..., example=1638941625786)


class EmptySearch(BaseModel):
    detail: str


class SearchDBCreate(SearchRequest):
    result: Union[SearchResponse, EmptySearch]


class Search(BaseModel):
    id: int
    city_id: int
    start_date: date = Field(..., example=date.today() - timedelta(days=30))
    end_date: date = Field(..., example=date.today())
    result: Union[SearchResponse, EmptySearch]

    class Config:
        orm_mode = True
