from fastapi import FastAPI, Depends, Response, status

from storage.db_io import store_animal, retrieve_animal, retrieve_animals_by_genus
from utils.db_dependency import g_get_session
from utils.models import Animal

app = FastAPI()


@app.get('/animal/{genus}/{species}')
async def get_animal(genus, species, response: Response, session=Depends(g_get_session)):
    animal = retrieve_animal(session, genus, species)
    if animal:
        return animal
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return animal


@app.get('/animal/{genus}')
async def get_animals(genus, session=Depends(g_get_session)):
    animals = retrieve_animals_by_genus(session, genus)
    return animals


@app.post('/animal', status_code=status.HTTP_200_OK)
async def post_animal(animal: Animal, session=Depends(g_get_session)):
    store_animal(session, animal)
    return {"inserted": True}
