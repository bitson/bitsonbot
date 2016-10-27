# Standard-Lib imports

# Third-Party imports

# BITSON Imports
from utils import *
from models.users import User

from logger import logger

logger.debug("Loading " + __name__ + " plugin...")


@bot.message_handler(commands=['start'])
def send_welcome(message):

    user_id = str(message.from_user.id)
    chat_id = str(message.chat.id)
    username = str(message.from_user.username)
    user = session.query(User).filter(User.telegram_id==user_id).first()
    if not user:
        if message.chat.type == 'private':
            bot.send_message(chat_id, text_messages['first_welcome'])
            user = User(telegram_id=user_id,
                        username=username,
                        private_chat=chat_id)
            session.add(user)
            session.commit()
    else:
        if message.chat.type == 'private':
            bot.send_message(chat_id, text_messages['welcome_again'])