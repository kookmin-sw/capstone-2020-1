from sqlalchemy import Column, Integer, String, ARRAY

from db import Base


class SoundHighlight(Base):
    __tablename__ = 'sound_highlight'

    id = Column(Integer, autoincrement=True, primary_key=True)
    url = Column(String, unique=True, nullable=False)
    highlight = Column(ARRAY(String, dimensions=2), nullable=False)
