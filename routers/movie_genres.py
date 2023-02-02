from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.movie_genres import Movie_Genres
from config.database import Session
from service.movie_genres import Movie_GenresService

movie_genres_router = APIRouter()

@movie_genres_router.get('/movie_genres', tags=['movie_genres'], response_model=Movie_Genres, status_code=200)
def get_movie_genres() -> Movie_Genres:
    db = Session()
    result = Movie_GenresService(db).get_movie_genres()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_genres_router.get('/movie/{id}/genres',tags=['movie_genres'])
def get_movie_genres_id(id: int = Path(ge=1,le=2000)):
    db = Session()
    result = Movie_GenresService(db).get_movie_genres_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_genres_router.post('/movie_genres', tags=['movie_genres'], status_code=201, response_model=dict)
def create_movie_genres(movie_genres: Movie_Genres) -> dict:
    db = Session()
    Movie_GenresService(db).create_movie_genres(movie_genres)
    return JSONResponse(content={'Message':'Movie genre saved in data base'})

@movie_genres_router.delete('/movie/{id}/genres',tags=['movie_genres'])
def delete_movie_genres(id:int):
    db = Session()
    result = Movie_GenresService(db).get_movie_genres_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    Movie_GenresService(db).delete_movie_genres(id)
    return JSONResponse(content="Delete movie genre", status_code=200)