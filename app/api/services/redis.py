import json
from datetime import timedelta

from api.schemas.search import SearchRequest, SearchResponse

from redis import Redis


class RedisClient(Redis):
    def __init__(self):
        Redis.__init__(self, host="redis")

    def __search_index(self, request: SearchRequest) -> str:
        return f"{request.city_id}-{request.start_date}-{request.end_date}"

    def set_search_result(self, request: SearchRequest, response: SearchResponse):
        self.setex(
            self.__search_index(request),
            timedelta(hours=1),
            json.dumps(response.dict()),
        )

    def get_search_result(self, request: SearchRequest) -> SearchResponse:
        result = self.get(self.__search_index(request))
        return SearchResponse(**json.loads(result)) if result else None
