from pydantic import BaseModel
from typing import Optional


class Movie_Genres(BaseModel):
    id: Optional[int] = None
    mov_id: int
    gen_id: int

    class Config:
        schema_extra = {
            'example':{
                'mov_id': 1,
                'gen_id': 1
            }
        }