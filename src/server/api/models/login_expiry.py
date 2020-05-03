import datetime

from sqlalchemy import Column, Integer, String, DateTime

from db import Base


class LoginExpiry(Base):
    __tablename__ = 'login_expiry'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=False)
    expiry = Column(DateTime, default=datetime.datetime.utcnow)
