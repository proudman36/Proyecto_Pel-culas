from models.rating import Rating as RatingModel
from schemas.rating import Rating

class RatingService():
    def __init__(self,db) -> None:
        self.db = db
    
    def get_rating(self) ->RatingModel:
        result = self.db.query(RatingModel).all()
        return result

    def get_rating_id(self,id:int):
        result = self.db.query(RatingModel).filter(RatingModel.rev_id == id).first()
        return result

    def create_rating(self,rating:RatingModel):
        new_rating = RatingModel(
            mov_id = rating.mov_id,
            rev_id = rating.rev_id,
            rev_stars = rating.rev_stars,
            num_o_ratings = rating.num_o_ratings
        )
        self.db.add(new_rating)
        self.db.commit()
        return
    
    def update_rating(self, id:int,data:Rating):
        self.db.query(RatingModel).filter(RatingModel.rev_id == id).first()
        Rating.id = data.id
        Rating.mov_id = data.mov_id
        Rating.rev_id = data.rev_id
        Rating.rev_stars = data.rev_stars
        Rating.num_o_ratings = data.num_o_ratings



    
    def delete_rating(self,id:int):
        self.db.query(RatingModel).filter(RatingModel.rev_id == id).delete()
        self.db.commit()
        return