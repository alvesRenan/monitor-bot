from logger import Log
from os import getenv

import telebot

from monitor_task import MonitorTask
from monitor_api import MonitorAPI

mercurio = telebot.TeleBot(getenv('API_KEY'))

@mercurio.message_handler(commands=['api'])
def res(message):
    MonitorAPI(mercurio, message.chat.id).run()

    mercurio.reply_to(message, f'Monitoramento iniciado, updates serão enviadas para este chat ({message.chat.title})')

@mercurio.message_handler(commands=['start'])
def res(message):
    MonitorTask(mercurio, message.chat.id, 'test-app').run()

    mercurio.reply_to(message, f'Monitoramento iniciado, updates serão enviadas para este chat ({message.chat.title})')

Log().log( 'Mercúrio está executando' )
mercurio.polling()