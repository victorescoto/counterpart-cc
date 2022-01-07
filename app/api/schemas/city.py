from pydantic import BaseModel, Field


class CityRequest(BaseModel):
    name: str = Field(..., example="Eusébio, CE")
    lat: float = Field(..., example=-3.854859)
    lon: float = Field(..., example=-38.4699622)


class CityResponse(CityRequest):
    id: int


class City(CityResponse):
    class Config:
        orm_mode = True
