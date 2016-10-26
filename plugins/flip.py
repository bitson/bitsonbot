# Standard-Lib imports

# Third-Party imports

# BITSON Imports
from utils import *
from logger import logger

logger.debug("Loading " + __name__ + " plugin...")


@bot.message_handler(commands=['flip'])
def flip(message):
    if in_time(message):
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        chat_id = str(message.chat.id)
        args = get_content(message)
        coin = ['cara', 'seca']
        if not args:
            bot.send_message(chat_id,
                             'Ingrese su elección... \n '
                             '¿cara o seca? \n'
                             '/flip <eleccion>',
                             parse_mode='Markdown')
            return
        if args != '-?' and args in coin:
            coin = random.choice(coin)
            if args == coin:
                bot.send_message(chat_id,
                                 'Salio %s. Ganaste.' % coin,
                                 parse_mode="Markdown")
            else:
                bot.send_message(chat_id,
                                 'Salio %s. Perdiste.' % coin,
                                 parse_mode="Markdown")
        elif args == '-?':
            bot.send_message(chat_id,
                             'Tira la moneda...  /flip <cara/seca>',
                             parse_mode='Markdown')
        else:
            bot.send_message(chat_id,
                             'La opción elegida es inválida.',
                             parse_mode='Markdown')