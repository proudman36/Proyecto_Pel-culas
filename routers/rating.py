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

@rating_router.post('/rating', tags=['rating'], status_code=201, response_model=dict)
def create_rating(rating:Rating) -> dict:
    db = Session()
    RatingService(db).create_rating(rating)
    return JSONResponse(content={'Message':'Rating saved in data base'})