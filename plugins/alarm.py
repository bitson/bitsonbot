
# Standard-Lib imports

# Third-Party imports

# BITSON Imports
from utils import *
from logger import logger


@bot.message_handler(commands=['set_alarm'])
def set_alarm(message):
    user_id = str(message.from_user.id)
    username = str(message.from_user.username)
    chat_id = str(message.chat.id)
    args = get_content(message)
    if not args:
        bot.send_message(chat_id=chat_id,
                         text='Debe ingresar todos los argumentos. \n'
                              '/set_alarm -? `o` /help `para obtener ayuda`',
                         parse_mode="Markdown")
        return
    args = args.split(',')
    if args[0] == '-?':
        bot.send_message(chat_id=chat_id,
                         text='`/set_alarm <HH:mm>, Mensaje a mostrar, repeat`\n'
                              '`<el campo repeat es optativo>`',
                         parse_mode="Markdown")
        return
    if len(args) < 3:
        args += '    norepeat'
    time, message, repeat = args
    if len(time.split(':')[0]) == 1:
        time = '0'+time
    alarms[time] = {
        'message': message,
        'repeat': repeat,
        'chat_id': chat_id,
    }
    bot.send_message(chat_id,
                     text_messages['set_alarm'],
                     parse_mode="Markdown")


@bot.message_handler(commands=['rem_alarm'])
def set_alarm(message):
    chat_id = str(message.chat.id)
    args = get_content(message)
    if not args:
        bot.send_message(chat_id=chat_id,
                         text='Debe ingresar todos los argumentos. \n'
                              '/rem_alarm -? `o` /help `para obtener ayuda`',
                         parse_mode="Markdown")
        return
    if args[0] == '-?':
        bot.send_message(chat_id=chat_id,
                         text='`/rem_alarm <HH:mm>`\n',
                         parse_mode="Markdown")
        return
    if len(args.split(':')[0]) == 1:
        args = '0' + args
    alarm = alarms.get(args) or None
    if alarms.get(args) and alarm.get('chat_id') == chat_id:
        del(alarms[args])
        bot.send_message(chat_id,
                         text_messages['rem_alarm'],
                         parse_mode="Markdown")
    else:
        bot.send_message(chat_id,
                         text='No hay alarmas para desactivar',
                         parse_mode="Markdown")


@bot.message_handler(commands=['show_alarms'])
def set_alarm(message):
    chat_id = str(message.chat.id)
    args = get_content(message)
    bot.send_message(chat_id=chat_id,
                     text=show_alarms(chat_id=chat_id),
                     parse_mode='Markdown')