import requests

from api.schemas.usgs import SearchParams, USGSResults


class USGSService:
    def __init__(self) -> None:
        self._base_url = "https://earthquake.usgs.gov"

    def search_earthquakes(self, search_params: SearchParams) -> USGSResults:
        query = {
            **search_params.dict(),
            "maxradius": 20,
            "minmagnitude": 5,
        }

        response = requests.get(
            f"{self._base_url}/fdsnws/event/1/query.geojson", params=query
        )

        return response.json()
