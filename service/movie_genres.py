from models.movie_genres import Movie_Genres as Movie_GenresModel

class Movie_GenresService():
    def __init__(self,db) -> None:
        self.db = db
    
    def get_movie_genres(self) -> Movie_GenresModel:
        result = self.db.query(Movie_GenresModel).all()
        return result
    
    def get_movie_genres_id(self,id:int):
        result = self.db.query(Movie_GenresModel).filter(Movie_GenresModel.gen_id == id).first()
        return result

    def create_movie_genres(self,movie_genres: Movie_GenresModel):
        new_movie_genres = Movie_GenresModel(
            mov_id = movie_genres.mov_id,
            gen_id = movie_genres.gen_id
        )
        self.db.add(new_movie_genres)
        self.db.commit()
        return

    def delete_movie_genres(self,id:int):
        self.db.query(Movie_GenresModel).filter(Movie_GenresModel.gen_id == id).delete()
        self.db.commit()
        return
        