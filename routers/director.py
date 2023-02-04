from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.director import Director
from config.database import Session
from service.director import DirectorService

director_router = APIRouter()

@director_router.get('/director', tags=['director'],response_model=Director,status_code=200)
def get_director() -> Director:
    db = Session()
    result = DirectorService(db).get_director()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@director_router.get('/director/{id}', tags=['director'])
def get_director_id(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = DirectorService(db).get_director_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@director_router.post('/director',tags=['director'], status_code=201, response_model=dict)
def create_director(director:Director) ->dict:
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={'Message':'Director saved in data base'})

@director_router.delete('/director/{id}',tags=['director'])
def delete_director(id:int):
    db = Session()
    result = DirectorService(db).get_director_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    DirectorService(db).delete_director(id)
    return JSONResponse(content="Delete director", status_code=200)
