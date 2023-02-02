from sqlalchemy import Column, Integer,ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Movie_Genres(Base):
    __tablename__ = 'movie_genres'
    id = Column(Integer,primary_key = True)
    mov_id = Column(Integer, ForeignKey('movie.id'))
    gen_id = Column(Integer, ForeignKey('genres.gen_id'))