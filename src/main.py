from os import environ
from threading import Thread

import telebot

from monitor_task import *

mercurio = telebot.TeleBot(environ('APP_KEY'))

@mercurio.message_handler(commands=['start'])
def res(message):
    Thread( target=monitor_task, args=(mercurio, message.chat.id, 'test-app') ).start()

    mercurio.reply_to(message, f'Monitoramento iniciado, updates serão enviadas para este chat ({message.chat.title})')

print( 'Mercúrio está executando' )
mercurio.polling()