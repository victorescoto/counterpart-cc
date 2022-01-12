import json
from datetime import timedelta
from typing import Union

from api.schemas.search import EmptySearch, SearchRequest, SearchResponse

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

    def get_search_result(
        self, request: SearchRequest
    ) -> Union[SearchResponse, EmptySearch]:
        result = self.get(self.__search_index(request))

        if not result:
            return None

        result = json.loads(result)

        if "detail" in result:
            return EmptySearch(**result)

        return SearchResponse(**result)
