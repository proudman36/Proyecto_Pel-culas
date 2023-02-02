from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.movie_direction import Movie_Direction
from config.database import Session
from service.movie_direction import Movie_DirectionService

movie_direction_router = APIRouter()

@movie_direction_router.get('/movie_direction',tags=['movie_direction'],response_model=Movie_Direction,status_code=200)
def get_movie_direction() ->Movie_Direction:
    db = Session()
    result = Movie_DirectionService(db).get_movie_direction()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_direction_router.get('movie/{id}/direction',tags=['movie_direction'])
def get_movie_direction_id(id:int = Path(ge = 1, le=2000)):
    db = Session()
    result = Movie_DirectionService(db).get_movie_direction_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_direction_router.post('/movie_direction',tags=['movie_direction'],status_code=201,response_model=dict)
def create_movie_direction(movie_direction:Movie_Direction) -> dict:
    db = Session()
    Movie_DirectionService(db).create_movie_direction(movie_direction)
    return JSONResponse(content={'Message':'Movie direction saved in data base'})

@movie_direction_router.delete('/movie/{id}/direction',tags=['movie_direction'])
def delete_movie_direction(id:int):
    db = Session()
    result = Movie_DirectionService(db).get_movie_direction_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    Movie_DirectionService(db).delete_movie_direction(id)
    return JSONResponse(content="Delete movie direction", status_code=200)
