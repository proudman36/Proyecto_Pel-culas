from typing import Optional
from pydantic import BaseModel, Field

class Director (BaseModel):
    dir_id: Optional[int] = None
    dir_fname: str = Field(max_length=15, min_length=1)
    dir_lname: str = Field(max_length=15,min_length=1)

    class Config:
        schema_extra = {
            'example':{
                'dir_fname': 'Martin',
                'dir_lname': 'Scorsese'
            }
        }
