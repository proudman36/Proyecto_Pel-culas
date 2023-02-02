from models.moviecast import MovieCast as MovieCastModel



class MovieCastService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_cast(self):
        result = self.db.query(MovieCastModel).all()
        return result

    def get_movie_cast_id(self,id_movie:int):
        result = self.db.query(MovieCastModel).filter(MovieCastModel.movie_id == id_movie).first()
        return result

    def create_movie_cast(self,movie_cast: MovieCastModel):
        new_cast = MovieCastModel(
            actor_id = movie_cast.actor_id,
            movie_id = movie_cast.movie_id,
            role = movie_cast.role
        )
        self.db.add(new_cast)
        self.db.commit()
        return

    def delete_movie_cast(self,id:int):
        self.db.query(MovieCastModel).filter(MovieCastModel.movie_id == id).delete()
        self.db.commit()
        return