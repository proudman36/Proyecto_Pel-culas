from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Movie_Cast:
    __tablename__ = 'movie_cast'
    id = Column(Integer, primary_key = True)
    actor_id = Column(Integer, ForeignKey('actor.id'))
    movie_id = Column(Integer, ForeignKey('movie.id'))
    role = Column(String)
    