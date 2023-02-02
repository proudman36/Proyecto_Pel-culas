from typing import Optional
from pydantic import BaseModel, Field

class Reviewer(BaseModel):
    rev_id: Optional[int] = None
    rev_name: str = Field(max_length=15, min_length=1)

    class Config:
        schema_extra = {
            'example':{
                'rev_name': 'Martin'
            }
        }