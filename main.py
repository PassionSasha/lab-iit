#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import telebot

bot = telebot.TeleBot('1076763292:AAE6xteIV1gqIfv3x27Ed5sIAYTraglvXDE')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "1":
        bot.send_message(message.from_user.id, "2")
    elif message.text == "41":
        bot.send_message(message.from_user.id, "55")

    elif message.text == "0":
        bot.send_message(message.from_user.id, "рнг")
    else:
        bot.send_message(message.from_user.id, "sluhayu")

bot.polling(none_stop=True, interval=2) 