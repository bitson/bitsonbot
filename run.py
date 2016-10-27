#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Standard lib Imports
import threading
# Third-Party Imports
import importdir
# BITSON Imports
from utils import *
from logger import logger
importdir.do('plugins', globals())


def run(mode='normal'):
    
    if mode == 'debug':
        logger.debug('Bot on debug mode...')
        bot.polling(True)
    
    else:
        logger.debug('Alarm process started')
        t = threading.Thread(target=verify_alarms)
        t.daemon = True
        t.start()
        logger.debug('Bot started...')
        bot.polling(none_stop=False, interval=0)


if __name__ == '__main__':
    # for debug mode run('debug')
    run()