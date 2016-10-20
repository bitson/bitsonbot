# Standard-Lib imports

# Third-Party imports

# BITSON Imports
from utils import *
from logger import logger

logger.debug("Loading " + __name__ + "...")


@bot.message_handler(commands=['flip'])
def flip(message):
    if in_time(message):
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        chat_id = str(message.chat.id)
        args = get_content(message)
        coin = ['cara', 'seca']
        if args != '-?':
                bot.send_message(chat_id,
                                 random.choice(coin),
                                 parse_mode="Markdown")
        elif args == '-?':
            bot.send_message(chat_id,
                             'Tira la moneda... <Próximamente interactivo!>')
        else:
            pass