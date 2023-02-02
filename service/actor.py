from models.actor import Actor as ActorModel

class ActorService():
    def __init__(self,db) -> None:
        self.db = db

    def get_actors(self) -> ActorModel:
        result = self.db.query(ActorModel).all()
        return result

    def get_actor(self,id:int):
        result = self.db.query(ActorModel).filter(ActorModel.id == id).first()
        return result

    def create_actor(self,actor:ActorModel):
        new_actor = ActorModel(
        actor_first_name = actor.actor_first_name ,
        actor_last_name = actor.actor_last_name,
        actor_gender = actor.actor_gender,    
        )
        self.db.add(new_actor)
        self.db.commit()
        return

    def delete_actor(self,id:int):
        self.db.query(ActorModel).filter(ActorModel.id == id).delete()
        self.db.commit()
        return

    