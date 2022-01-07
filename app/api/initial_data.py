from api.core import database, models
from api.crud import city as city_crud
from api.schemas.city import CityRequest


def setup_tables():
    models.Base.metadata.create_all(bind=database.engine)


def main():
    setup_tables()

    city_crud.create_city(
        database.SessionLocal(),
        CityRequest(name="Los Angeles, CA", lat=34.0522342, lon=-118.2436849),
    )
    city_crud.create_city(
        database.SessionLocal(),
        CityRequest(name="San Francisco, CA", lat=37.7749295, lon=-122.4194155),
    )
    city_crud.create_city(
        database.SessionLocal(),
        CityRequest(name="Tokyo, Japan", lat=35.652832, lon=139.839478),
    )


if __name__ == "__main__":
    main()
