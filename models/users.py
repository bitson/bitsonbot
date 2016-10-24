
# Standard-Lib imports
from sqlalchemy import Column, String, Integer
from sqlalchemy import Sequence
# Third-Party imports

# BITSON Imports
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True)
    username = Column(String(200))
    telegram_id = Column(Integer)
