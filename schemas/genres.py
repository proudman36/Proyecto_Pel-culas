from typing import Optional
from pydantic import BaseModel, Field

class Genre(BaseModel):
    gen_id: Optional[int] = None
    gen_title: str = Field(max_length=15,min_length=1)
    
    class config:
        schema_extra = {
            'example':{
                'genre_title':'Action'
            }
        }