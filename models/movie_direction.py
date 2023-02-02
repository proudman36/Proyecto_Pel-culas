from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Movie_Direction(Base):
    __tablename__  = 'movie_direction'

    id = Column(Integer,primary_key = True)
    dir_id = Column(Integer, ForeignKey('director.dir_id'))
    mov_id = Column(Integer, ForeignKey('movie.id'))