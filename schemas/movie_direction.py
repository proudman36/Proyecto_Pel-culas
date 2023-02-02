from typing import Optional
from pydantic import BaseModel

class Movie_Direction(BaseModel):
    id: Optional[int] = None
    dir_id: int
    mov_id: int

    class Config:
        schema_extra = {
            'example':{
                'dir_id': 1,
                'mov_id': 1
            }
        }