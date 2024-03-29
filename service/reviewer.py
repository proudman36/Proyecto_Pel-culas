from models.reviewer import Reviewer as ReviewerModel
from schemas.reviewer import Reviewer

class ReviewerService():
    def __init__(self,db) -> None:
        self.db = db 

    def get_reviewer(self)  ->ReviewerModel:
        result = self.db.query(ReviewerModel).all()
        return result

    def get_reviewer_id(self,id:int):
        result = self.db.query(ReviewerModel).filter(ReviewerModel.rev_id == id).first()
        return result
    
    def create_reviewer(self, reviewer: ReviewerModel):
        new_reviewer = ReviewerModel(
            rev_id = reviewer.rev_id,
            rev_name = reviewer.rev_name
        )
        self.db.add(new_reviewer)
        self.db.commit()
        return 

    def update_reviewer(self,id:int,reviewer:ReviewerModel):
        self.db.query(ReviewerModel).filter(ReviewerModel.rev_id == id).first()
        Reviewer.rev_id = reviewer.rev_id
        Reviewer.rev_name = reviewer.rev_name

    def delete_reviewer(self,id:int):
        self.db.query(ReviewerModel).filter(ReviewerModel.rev_id == id).delete()
        self.db.commit()
        return