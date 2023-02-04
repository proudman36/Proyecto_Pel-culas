from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.rating import Rating
from config.database import Session
from service.rating import RatingService

rating_router = APIRouter()

@rating_router.get('/rating', tags=['rating'], response_model=Rating, status_code=200)
def get_rating() -> Rating:
    db = Session()
    result = RatingService(db).get_rating()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@rating_router.get('/rating/{id}',tags=['rating'])
def get_rating_id(id:int = Path(ge=1, le=2000)):
    db = Session()
    result = RatingService(db).get_rating_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@rating_router.post('/rating', tags=['rating'], status_code=201, response_model=dict)
def create_rating(rating:Rating) -> dict:
    db = Session()
    RatingService(db).create_rating(rating)
    return JSONResponse(content={'Message':'Rating saved in data base'})

@rating_router.delete('/rating/{id}',tags=['rating'])
def delete_rating(id:int):
    db = Session()
    result = RatingService(db).get_rating_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    RatingService(db).delete_rating(id)
    return JSONResponse(content="Delete rating", status_code=200)
