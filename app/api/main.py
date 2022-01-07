from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import city, search


def create_app():
    app = FastAPI(title="Counterpart Challenge", redoc_url=None)

    app.include_router(city.router)
    app.include_router(search.router)

    origins = [
        "http://localhost",
        "http://localhost:8081",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()
