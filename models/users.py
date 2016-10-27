#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Standard lib Imports

# Third Party Imports
from sqlalchemy import Column, String, Integer, Boolean
# BITSON Imports
from utils import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(200))
    telegram_id = Column(Integer)
    private_chat = Column(Integer)
    admin = Column(Boolean, default=False)
    banned = Column(Boolean, default=False)
