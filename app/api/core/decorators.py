from functools import wraps

from api.services.redis import RedisClient


def cached(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        redis_client = RedisClient()
        cached_response = redis_client.get_search_result(kwargs["request_params"])

        if cached_response:
            return cached_response

        response = func(*args, **kwargs)
        redis_client.set_search_result(kwargs["request_params"], response)

        return response

    return wrapper
