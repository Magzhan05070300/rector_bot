import os
from flask import Flask, request
import sqlite3
import telebot
from telebot import types
import telebot
from telebot import types

TOKEN = '5783909335:AAHceVgsYSeA7qqu1Q_lh7g8GQziZrBryM8'
APP_URL = f'https://jenpulineochered.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
chat_id = '473641296'

knopka1 = 'Академиялық қызмет жөніндегі проректор'
knopka2 = 'Инфрақұрылымдық даму жөніндегі проректор'
knopka3 = 'Ғылыми жұмыс жөніндегі проректор'
knopka4 = 'Стратегиялық даму жөніндегі проректор'
knopka5 = 'Басқа құрылымға'


@bot.message_handler(commands=["start"])
def first(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.add(knopka1)
    keyboard.add(knopka2)
    keyboard.add(knopka3)
    keyboard.add(knopka4)
    send = bot.send_message(message.chat.id, 'Қажет құрылымды таңдаңыз!', parse_mode='Markdown',
                            reply_markup=keyboard)
    bot.register_next_step_handler(send, second)


def second(message):
    # bot.send_message(chat_id=chat_id, text=message.text)

    if message.text == knopka1:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=473641296, text=knopka1)
        send = bot.send_message(message.chat.id,
                                'Аты-жөніңізді, почтаңызды және ұсынысыңызды жазыңыз болмаса кездесу күнін белгілеңіз (День.Месяц.Год)',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka2:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=473641296, text=knopka2)
        send = bot.send_message(message.chat.id,
                                'Аты-жөніңізді, почтаңызды және ұсынысыңызды жазыңыз болмаса кездесу күнін белгілеңіз (День.Месяц.Год',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka3:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=473641296, text=knopka3)
        send = bot.send_message(message.chat.id,
                                'Аты-жөніңізді, почтаңызды және ұсынысыңызды жазыңыз болмаса кездесу күнін белгілеңіз (День.Месяц.Год',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka4:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=473641296, text=knopka4)
        send = bot.send_message(message.chat.id,
                                'Аты-жөніңізді, почтаңызды және ұсынысыңызды жазыңыз болмаса кездесу күнін белгілеңіз (День.Месяц.Год',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    
   elif message.text == knopka5:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=473641296, text=knopka5)
        send = bot.send_message(message.chat.id,
                                'Аты-жөніңізді, почтаңызды және ұсынысыңызды жазыңыз болмаса кездесу күнін белгілеңіз (День.Месяц.Год',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second)


def third(message):
    bot.send_message(chat_id=473641296, text=message.text)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
