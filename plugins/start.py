
# Standard-Lib imports

# Third-Party imports

# BITSON Imports
from utils import *
from logger import logger


logger.debug("Loading " + __name__ + "...")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = str(message.from_user.id)
    chat_id = str(message.chat.id)
    
    if message.chat.type == 'private':
        bot.send_message(chat_id, text_messages['welcome'])