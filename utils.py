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

text_messages = {
    'help': 'Estas son todas las cosas que puedo hacer...\n'
            '`>` /help\n'
            '`>` /flip\n'
            'Un monton, no?\n'
            'Ingresá /<comando> "-?" para mas información',
    'help_group':
        u"`Mejor no spammear en {title}... Te envío un MP con la ayuda`",
    'welcome': "Bienvenido al bot de Bitson.\n"
               "Puede solicitar ayuda ingresando /help... o llamando al 911 "
               "(dependiendo de que tipo de ayuda necesite)"
    
}