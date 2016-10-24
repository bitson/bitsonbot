# Standard-Lib imports

# Third-Party imports

# BITSON Imports
from utils import *
from logger import logger
from models.users import User
from bitsonbot import db

logger.debug("Loading " + __name__ + "...")


@bot.message_handler(commands=['help_with_db'])
def help(message):
    if in_time(message):
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        chat_id = str(message.chat.id)
        args = get_content(message)
        
        registered_users = [user.telegram_id for user in db.query(User).filter().all()]
        if not args:
            if message.chat.type == 'private':
                bot.send_message(chat_id,
                                 text_messages['help'])
            elif message.chat.type == 'group' \
                    or message.chat.type == 'supergroup':
                if user_id in registered_users:
                    bot.send_message(user_id,
                                     text_messages['help'],
                                     parse_mode="Markdown")
                    
                    bot.reply_to(message,
                                 text_messages['help_group'].format(
                                     title=message.chat.title),
                                 parse_mode="Markdown")
                else:
                    bot.reply_to(message,
                                 text_messages['help_group_first'].format(
                                     title=message.chat.title),
                                 parse_mode="Markdown")
        elif args == '-?':
            bot.send_message(chat_id,
                             'En serio? Necesitas ayuda sobre la ayuda?... '
                             'Anda a dormir @%s' % username)
