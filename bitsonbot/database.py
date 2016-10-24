#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Standard lib imports
# Third Party imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from bitsonbot.logger import logger

DB_STRING = 'postgresql://bitsonbot:bitson@localhost:5432/bitsonbot'

# DB CONFIGURATION
logger.debug('Creating db connection')
engine = create_engine(DB_STRING)

Base = declarative_base()

Session = sessionmaker(bind=engine)
db = Session()
Base.metadata.create_all(engine)