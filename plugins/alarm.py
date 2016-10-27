
# Standard-Lib imports

# Third-Party imports

# BITSON Imports
from utils import *
from logger import logger
from models.alarms import Alarm


logger.debug("Loading " + __name__ + " plugin...")


@bot.message_handler(commands=['set_alarm'])
def set_alarm(message):
    user_id = str(message.from_user.id)
    username = str(message.from_user.username)
    chat_id = str(message.chat.id)
    args = get_content(message)
    try:
        if not args:
            bot.send_message(chat_id=chat_id,
                             text='Debe ingresar todos los argumentos. \n'
                                  '/set_alarm -? `o` /help `para obtener ayuda`',
                             parse_mode="Markdown")
            return
        args = args.split(', ')
        if len(args) == 1:
            args = args[0].split(',')
        if args[0] == '-?':
            bot.send_message(chat_id=chat_id,
                             text='`/set_alarm <HH:mm>, Mensaje a mostrar, repeat`\n'
                                  '`<el campo repeat es optativo>`',
                             parse_mode="Markdown")
            return
        if len(args) < 3:
            args.append(None)
        time, message, repeat = args
        if len(time.split(':')[0]) == 1:
            time = '0'+time
        try:
            alarm = Alarm(hour=time,
                          message=message,
                          repeat= True if repeat else False,
                          chat_id=chat_id,
                          user_id=user_id)
            session.add(alarm)
            session.commit()
            bot.send_message(chat_id,
                             text_messages['set_alarm'],
                             parse_mode="Markdown")
        except Exception as ex:
            bot.send_message(chat_id=chat_id,
                             text='Verifique los argumentos ingresados \n'
                                  '/set_alarm -? `o` /help `para obtener ayuda`',
                             parse_mode="Markdown")
    except:
        bot.send_message(chat_id=chat_id,
                         text='Verifique los argumentos ingresados \n'
                              '/set_alarm -? `o` /help `para obtener ayuda`',
                         parse_mode="Markdown")


@bot.message_handler(commands=['rem_alarm'])
def rem_alarm(message):
    user_id = str(message.from_user.id)
    chat_id = str(message.chat.id)
    args = get_content(message)
    if not args:
        bot.send_message(chat_id=chat_id,
                         text='`Comando invalido. Ingrese /rem_alarm -?`',
                         parse_mode="Markdown")
        return
    if args == '-?':
        bot.send_message(chat_id=chat_id,
                         text='`/rem_alarm <HH:mm>`\n',
                         parse_mode="Markdown")
        return
    if len(args.split(':')[0]) == 1:
        args = '0' + args
    alarms = session.query(Alarm).filter(Alarm.chat_id==chat_id,
                                        Alarm.hour==args,
                                        Alarm.enable==True,
                                        Alarm.user_id==user_id).all()
    if not alarms:
        bot.send_message(chat_id,
                         text='No hay alarmas para desactivar',
                         parse_mode="Markdown")
        return

    for alarm in alarms:
        alarm.enable = False
        alarm.repeat = False
        session.commit()
    bot.send_message(chat_id,
                     text_messages['rem_alarm'],
                     parse_mode="Markdown")


@bot.message_handler(commands=['show_alarms'])
def show_alarms(message):
    chat_id = str(message.chat.id)
    args = get_content(message)
    alarms = session.query(Alarm).filter(Alarm.chat_id==chat_id,
                                         Alarm.enable==True).order_by(Alarm.hour).all()
    message = str()
    if not alarms:
        message = 'No hay alarmas para mostrar'
    for alarm in alarms:
        message += '`%s - %s \n`' %(alarm.hour, alarm.message)

    bot.send_message(chat_id=chat_id,
                     text=message,
                     parse_mode='Markdown')