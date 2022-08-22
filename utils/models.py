from pydantic import BaseModel
from typing import List

class Animal(BaseModel):
    genus: str
    species: str
    image_url: str
    size_cm: float
    sightings: int
    taxonomy: List[str]

class Plant(BaseModel):
    genus: str
    species: str
    sightings: int
