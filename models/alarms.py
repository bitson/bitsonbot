#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Standard lib Imports

# Third Party Imports
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import Sequence
# BITSON Imports
from utils import Base


class Alarm(Base):
    __tablename__ = 'alarms'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(200))
    chat_id = Column(Integer)
    hour = Column(Integer)
    message = Column(String(500))
    enable = Column(Boolean)
