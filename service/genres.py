from models.genres import Genre as GenreModel

class GenreService():
    def __init__(self,db) -> None:
        self.db = db 
    
    def get_genres(self) -> GenreModel:
        result = self.db.query(GenreModel).all()
        return result

    def get_genre(self,id:int):
        result = self.db.query(GenreModel).filter(GenreModel.gen_id == id).first()
        return result

    def create_genres(self,genre: GenreModel):
        new_genre = GenreModel(
            gen_id = genre.gen_id,
            gen_title = genre.gen_title
        )
        self.db.add(new_genre)
        self.db.commit()
        return
    
    def delete_genres(self,id:int):
        self.db.query(GenreModel).filter(GenreModel.gen_id == id).delete()
        self.db.commit()
        return