#! /usr/bin/env python
# -*- coding:utf-8 -*-

# Standard lib imports
from datetime import datetime
import random
import re
import time

# Third Party imports
import telebot

# BITSON Imports
from logger import logger

bot = telebot.TeleBot('181427227:AAEE664QqZ0oGafEm3Kmp8P0ttObrDHQdv4')


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


def verify_alarms(alarms=None):
    while True:
        now = datetime.now().strftime('%H:%M')
        alarm = alarms.get(now) or None
        if alarm:
            try:
                bot.send_message(chat_id=alarm.get('chat_id'),
                                 text=alarm.get('message'))
            except Exception:
                logger.error(Exception)
            finally:
                if alarm.get('repeat') == 'norepeat':
                    del(alarms[now])
                else:
                    while now == datetime.now().strftime('%H:%M'):
                        pass


def show_alarms(chat_id=None):
    alarm_keys = list(alarms.keys())
    alarm_keys.sort()
    response = str()
    for key in alarm_keys:
        if alarms[key]['chat_id'] == chat_id:
            response += "`%s - %s `\n" % (key, alarms[key]['message'])
    if not response:
        response = '`No hay alarmas para mostrar`'
    return response

alarms = {
    # 'HH:mm':{'message': 'message',
    #          'repeat': False,
    #          'channel_id': channel_id }
}

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
    'welcome': "Bienvenido al bot de Bitson.\n"
               "Puede solicitar ayuda ingresando /help... o llamando al 911 "
               "(dependiendo de que tipo de ayuda necesite)",
    'set_alarm': "Alarma configurada.",
    'rem_alarm': "Alarma desactivada.",
}