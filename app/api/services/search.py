from typing import List

from api.schemas.search import EarthquakeDistance
from api.schemas.usgs import USGSResults
from haversine import haversine


class SearchService:
    def _calculate_distance(self, coordinates: list, city) -> float:
        return haversine((city.lat, city.lon), coordinates)

    def format_USGS_results(
        self, results: USGSResults, city
    ) -> List[EarthquakeDistance]:
        return [
            EarthquakeDistance(
                title=feature["properties"]["title"],
                time=feature["properties"]["time"],
                distance=self._calculate_distance(
                    feature["geometry"]["coordinates"][:-1], city
                ),
            )
            for feature in results["features"]
        ]

    def get_nearest_earthquake(
        self, results: List[EarthquakeDistance]
    ) -> EarthquakeDistance:
        results.sort(key=lambda x: x.distance)
        return results[0]
