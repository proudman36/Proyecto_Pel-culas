from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.reviewer import Reviewer
from config.database import Session
from service.reviewer import ReviewerService

reviewer_router = APIRouter()

@reviewer_router.get('/reviewer',tags=['reviewer'],response_model=Reviewer,status_code=200)
def get_reviewer() -> Reviewer:
    db = Session()
    result = ReviewerService(db).get_reviewer()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@reviewer_router.post('/reviewer',tags=['reviewer'],status_code=201,response_model=dict)
def create_reviewer(reviewer:Reviewer) ->dict:
    db = Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse(content={'Message':'Reviewer saved in data base'})

@reviewer_router.get('/reviewer/{id}', tags=['reviewer'])
def get_genre(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = ReviewerService(db).get_reviewer_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)  

@reviewer_router.put('/reviewer/{id}',tags=['reviewer'])
def update_rating(id:int, reviewer:Reviewer):
    db = Session()
    result = ReviewerService(db).get_reviewer_id(id)
    if not result:
        return JSONResponse(content={'message':'Register not found','status code':'404'})
    ReviewerService(db).update_reviewer(id,reviewer)
    return JSONResponse(content={'message':'The reviewer with the id {id} was modified'})

@reviewer_router.delete('/reviewer/{id}',tags=['reviewer'])
def delete_reviewer(id:int):
    db = Session()
    result = ReviewerService(db).get_reviewer_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    ReviewerService(db).delete_reviewer(id)
    return JSONResponse(content="Delete reviewer", status_code=200)



