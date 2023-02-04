from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.actor import Actor
from config.database import Session
from service.actor import ActorService


actor_router = APIRouter()

@actor_router.get('/actors',tags=['actors'], response_model=Actor, status_code= 200)
def get_actor() ->Actor:   
    db = Session()
    result = ActorService(db).get_actors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@actor_router.get('/actors/{id}', tags=['actors'])
def get_actor_id(id:int = Path(ge= 1, le=2000)):
    db = Session()
    result = ActorService(db).get_actor(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@actor_router.post('/actors', tags=['actors'], status_code=201 , response_model=dict)
def create_actor(actor:Actor) ->dict:
    db= Session()
    ActorService(db).create_actor(actor)
    return JSONResponse(content={'message':'actor save in data base'})

@actor_router.delete('/actors/{id}',tags=['actors'])
def delete_actor(id:int):
    db = Session()
    result = ActorService(db).get_actor(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    ActorService(db).delete_actor(id)
    return JSONResponse(content="Delete actor", status_code=200)


