from db import Base
from sqlalchemy import Column, Integer, String, Unicode


class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    pw = Column(String, nullable=False)
    name = Column(Unicode, nullable=False)
    age = Column(String, nullable=False)
