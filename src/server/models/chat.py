from sqlalchemy import Column, Integer, String, UniqueConstraint, JSON

from db import Base


class Keyword(Base):
    __tablename__ = 'top_keyword'

    id = Column(Integer, primary_key=True, autoincrement=True)
    platform = Column(String, nullable=False)
    videoid = Column(String, nullable=False)
    keyword_json = Column(JSON, nullable=False)

    __table_args__ = (
        UniqueConstraint('platform', 'videoid'),
    )
