from pydantic import BaseModel
from datetime import date


class Property(BaseModel):
    title: str
    time: int


class Geometry(BaseModel):
    coordinates: list


class Feature(BaseModel):
    properties: Property
    geometry: Geometry


class USGSResults(BaseModel):
    features: Feature


class SearchParams(BaseModel):
    starttime: date
    endtime: date
    latitude: float
    longitude: float
