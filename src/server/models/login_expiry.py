import datetime
import uuid

from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy_utils import UUIDType

from db import Base


class LoginExpiry(Base):
    __tablename__ = 'login_expiry'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(UUIDType, primary_key=True, default=uuid.uuid4, nullable=False)
    email = Column(String, nullable=False, unique=False)
    name = Column(String, nullable=True, unique=False)
    expiry = Column(DateTime, default=datetime.datetime.now)

    __table_args__ = (
        UniqueConstraint('uuid', 'email'),
    )
