
from pydantic import BaseModel, Field
from typing import Optional



class MovieCast(BaseModel):
        id: Optional[int] = None
        actor_id: int
        movie_id: int
        role: str = Field(max_length=30,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    "actor_id": 1,
                    "movie_id":1,
                    "role":"Part of family"
                }
            }
