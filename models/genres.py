from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Genre(Base):
    __tablename__ = 'genres'
    gen_id = Column(Integer,primary_key=True)
    gen_title = Column(String)
