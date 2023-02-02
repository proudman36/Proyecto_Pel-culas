from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_cast import MovieCast
from service.movie_cast import MovieCastService


movie_cast_router = APIRouter()


@movie_cast_router.get('/movie/{id_movie}/cast/', tags=['movie_cast'],response_model=list[MovieCast],status_code=200)
def get_movie_cast(id_movie:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieCastService(db).get_movie_cast_id(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_cast_router.get('/movie_cast', tags=['movie_cast'], response_model=MovieCast, status_code=200)
def get_movie_cast() -> MovieCast:
    db = Session()
    result = MovieCastService(db).get_movie_cast()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_cast_router.post('/movie_cast', tags=['movie_cast'],response_model=dict,status_code=201)
def create_cast(cast:MovieCast)->dict:
    db = Session()
    MovieCastService(db).create_movie_cast(cast)
    return JSONResponse(content={"message":"Se ha registrado el actor","status_code":201})

@movie_cast_router.delete('/movie_cast/{id}',tags=['movie_cast'])
def movie_cast_delete(id:int):
    db = Session()
    result = MovieCastService(db).get_movie_cast_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    MovieCastService(db).delete_movie_cast(id)
    return JSONResponse(content="Delete cast", status_code=200)
