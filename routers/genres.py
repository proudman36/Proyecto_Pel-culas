from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.genres import Genre
from config.database import Session
from service.genres import GenreService



genres_router = APIRouter()

@genres_router.get('/genres', tags=['genres'], response_model=Genre, status_code=200)
def get_genre () -> Genre:
    db =  Session()
    result = GenreService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@genres_router.post('/genres', tags=['genres'], status_code=201, response_model=dict)
def create_genre(genre:Genre) -> dict:
    db = Session()
    GenreService(db).create_genres(genre)
    return JSONResponse(content={'Message':'Genre saved in data base'})

@genres_router.get('/genres/{id}',tags=['genres'])
def get_genre(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = GenreService(db).get_genre(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@genres_router.delete('/genres/{id}', tags=['genres'])
def genres_delete(id:int):
    db = Session()
    result = GenreService(db).get_genre(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    GenreService(db).delete_genres(id)
    return JSONResponse(content="Delete genres", status_code=200)


