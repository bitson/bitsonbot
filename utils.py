#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Standard lib Imports
import time
import sys
from datetime import datetime
import random
import re
# Third-Party Imports
import telebot
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from logger import logger

try:
    TOKEN = str(sys.argv[1])
    bot = telebot.TeleBot(TOKEN)
except:
    print('Debe ingresar el token.')


DB_STRING = 'postgresql://bitsonbot:bitson@localhost:5432/bitsonbot'

# DB CONFIGURATION
logger.debug("Starting DB Connection")
engine = create_engine(DB_STRING)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_content(text):
    command = re.findall(r'/{1}\w+[@bitsonBot]*\s+(.*)', text.text,
                         re.DOTALL)
    if command:
        whole = ""
        for line in command:
            if line == "":
                whole += "\n"
            else:
                whole += line
        return whole
    else:
        pass


def in_time(message):
    """ this function check if the message it's too old... """
    time_range = time.mktime(datetime.now().timetuple())
    if int(time_range - message.date) < 10:
        if not message.forward_from:
            return True
    else:
        return False


def verify_alarms():
    from models.alarms import Alarm
    while True:
        now = datetime.now().strftime('%H:%M')
        alarms = session.query(Alarm).filter(Alarm.enable==True,
                                            Alarm.hour==now).all()
        try:
            for alarm in alarms:
                bot.send_message(chat_id=alarm.chat_id,
                                 text=alarm.message)
                if not alarm.repeat:
                    alarm.enable = False
        except Exception as ex:
            logger.error(ex)
        finally:
            session.commit()
            while now == datetime.now().strftime('%H:%M'):
                pass


text_messages = {
    'help': 'Estas son todas las cosas que puedo hacer...\n'
            '> /help\n'
            '> /flip <cara/seca>\n'
            '> /set_alarm HH:MM, message, <repeat/norepeat>\n'
            '> /rem_alarm HH:MM\n'
            '> /show_alarms \n'
            'Un monton, no?\n'
            'Ingresá /<comando> "-?" para mas información',
    'help_group':
        u"`Mejor no spammear en {title}... Te envío un MP con la ayuda`",
    'help_group_first':
        u"Primero enviame /start por privado a @bitsonbot asi puedo "
        u"empezar a hablarte",
    'first_welcome': "Bienvenido al bot de Bitson.\n"
               "Puede solicitar ayuda ingresando /help... o llamando al 911 "
               "(dependiendo de que tipo de ayuda necesite)",
    'welcome_again': "Bueno... con un /start estamos bien.\n"
               "Puede solicitar ayuda ingresando /help... ",
    'set_alarm': "Alarma configurada.",
    'rem_alarm': "Alarma desactivada.",
    
}