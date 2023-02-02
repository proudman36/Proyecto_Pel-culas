from models.rating import Rating as RatingModel

class RatingService():
    def __init__(self,db) -> None:
        self.db = db
    
    def get_rating(self) ->RatingModel:
        result = self.db.query(RatingModel).all()
        return result

    def create_rating(self,rating:RatingModel):
        new_rating = RatingModel(
            mov_id = rating.mov_id,
            rev_id = rating.rev_id,
            rev_stars = rating.rev_stars,
            num_o_rating = rating.num_o_ratings
        )
        self.db.add(new_rating)
        self.db.commit()
        return
        