#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Standard lib imports
import threading
# Third Party imports

# BITSON Imports
import importdir
from utils import *
from logger import logger
from database import db

importdir.do('plugins', globals())


def run(mode='normal'):
    if mode == 'debug':
        logger.debug('Bot on debug mode...')
        bot.polling(True)

    else:
        logger.debug('Alarm process started')
        t = threading.Thread(target=verify_alarms, args=[alarms,])
        t.daemon = True
        t.start()
        logger.debug('Bot started...')
        bot.polling(none_stop=False, interval=0)
        


if __name__ == '__main__':
    # for debug mode run('debug')
    run()