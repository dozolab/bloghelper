# library
import telebot

# django
from django.http.response import HttpResponse
from django.conf import settings

from apps.telegram import db_connection
from apps.telegram.views.bot import (
    start_message_view, send_message_view
)

bot = telebot.TeleBot(settings.BOT_TOKEN)


def web_hook_view(request):
    if request.method == 'POST':
        bot.process_new_updates([telebot.types.Update.de_json(request.body.decode('utf-8'))])
        return HttpResponse('ok')
    return HttpResponse('ok')


@bot.message_handler(commands=['start'])
def start_message_request(message):
    print(message.text)
    start_message_view(message, bot)


@bot.message_handler(func=lambda message: True)
def text_message_handler(message):
    send_message_view(message, bot)


# @bot.message_handler(content_types=['contact'])
# def contact_message_handler(message):
#     contact_message_view(message, bot)
#
#
# @bot.message_handler(func=lambda message: True)
# def text_message_handler(message):
#     step_message_controller_view(message, bot)
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message_controller_handler(callback):
#     callback_message_controller_view(callback, bot)
