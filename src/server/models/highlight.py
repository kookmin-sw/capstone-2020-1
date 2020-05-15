from sqlalchemy import Column, Integer, String, JSON

from db import Base


class SoundHighlight(Base):
    __tablename__ = 'sound_highlight'

    id = Column(Integer, autoincrement=True, primary_key=True)
    url = Column(String, unique=True, nullable=False)
    highlight_json = Column(JSON, nullable=False)


class ChatHighlight(Base):
    __tablename__ = 'chat_highlight'

    id = Column(Integer, autoincrement=True, primary_key=True)
    platform = Column(String, nullable=False)
    videoid = Column(String, nullable=False, unique=True)
    highlight_json = Column(JSON, nullable=False)
