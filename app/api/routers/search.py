from typing import List, Union

from api.core.dependencies import get_db
from api.crud import city as city_crud
from api.crud import search as search_crud
from api.schemas.search import (
    EmptySearch,
    Search,
    SearchDBCreate,
    SearchRequest,
    SearchResponse,
)
from api.schemas.usgs import SearchParams
from api.services.redis import RedisClient
from api.services.search import SearchService
from api.services.usgs import USGSService
from fastapi import APIRouter, Depends, HTTPException
from requests.exceptions import ConnectionError
from sqlalchemy.orm.session import Session

router = APIRouter()


@router.get("/search", response_model=List[Search], tags=["search"])
def list_searches(db: Session = Depends(get_db)):
    return search_crud.get_searches(db)


@router.post(
    "/search", response_model=Union[SearchResponse, EmptySearch], tags=["search"]
)
def search(
    request_params: SearchRequest,
    db: Session = Depends(get_db),
    usgs_service: USGSService = Depends(USGSService),
    search_service: SearchService = Depends(SearchService),
    redis_client: RedisClient = Depends(RedisClient),
):
    response = redis_client.get_search_result(request_params)
    if response:
        return response

    city = city_crud.get_city(db, request_params.city_id)

    if not city:
        raise HTTPException(status_code=400, detail="Invalid city!")

    try:
        usgs_search_params = SearchParams(
            starttime=request_params.start_date,
            endtime=request_params.end_date,
            latitude=city.lat,
            longitude=city.lon,
        )
        usgs_search_result = usgs_service.search_earthquakes(usgs_search_params)
    except ConnectionError:
        raise HTTPException(status_code=500, detail="Something went wrong")

    try:
        results = search_service.format_USGS_results(usgs_search_result, city)
        result = search_service.get_nearest_earthquake(results)
    except IndexError:
        return EmptySearch(detail="No results found")

    response = SearchResponse(city_name=city.name, title=result.title, time=result.time)

    search = SearchDBCreate(**request_params.dict(), result=response)
    search_crud.create_search(db, search)

    redis_client.set_search_result(request_params, response)

    return response
