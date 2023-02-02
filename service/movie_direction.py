from models.movie_direction import Movie_Direction as Movie_DirectionModel

class Movie_DirectionService():
    def __init__(self,db) -> None:
        self.db = db

    def get_movie_direction(self) -> Movie_DirectionModel:
        result = self.db.query(Movie_DirectionModel).all()
        return result

    def get_movie_direction_id(self,id:int):
        result = self.db.query(Movie_DirectionModel).filter(Movie_DirectionModel.dir_id == id).first()
        return result

    def create_movie_direction(self,movie_direction: Movie_DirectionModel):
        new_movie_direction = Movie_DirectionModel(
            dir_id = movie_direction.dir_id,
            mov_id = movie_direction.mov_id
        )
        self.db.add(new_movie_direction)
        self.db.commit()
        return

    def delete_movie_direction(self,id:int):
        self.db.query(Movie_DirectionModel).filter(Movie_DirectionModel.dir_id ==  id).delete()
        self.db.commit()
        return

