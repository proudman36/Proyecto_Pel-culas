from pydantic import BaseModel
from typing import Optional

class Rating(BaseModel):
    id: Optional[int] = None
    mov_id: int
    rev_id: int
    rev_stars:int
    num_o_ratings:int

    class Config:
        schema_extra = {
            'example':{
                'mov_id':1,
                'rev_id':1,
                'rev_stars':1,
                'num_o_ratings':1
            }
        }