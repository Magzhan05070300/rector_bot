import os
from flask import Flask, request
import sqlite3
import telebot
from telebot import types
import telebot
from telebot import types

TOKEN = '5781509389:AAGsC_eoDQPAGnrKNcqf-kbb6wRH19vFm2o'
APP_URL = f'https://remarkable-cuchufli-424fb8.netlify.app/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
#chat_id = '609240271'

knopka1 = 'Академиялық қызмет жөніндегі проректор'
knopka2 = 'Инфрақұрылымдық даму жөніндегі проректор'
knopka3 = 'Ғылыми жұмыс жөніндегі проректор'
knopka4 = 'Стратегиялық даму жөніндегі проректор'
knopka5 = 'Басқа құрылымға'
knopka6 = 'Қазақ тілі'
knopka7 = 'Русский язык'
knopka8 = 'Проректор по академическим вопросам'
knopka9 = 'Проректор по инфраструктурному развитию'
knopka10 = 'Проректор по науке'
knopka11 = 'Проректор по стратегическому развитию'
knopka12 = 'Другие подразделения'
knopka13 = ''

@bot.message_handler(commands=["start"])
def bir(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.add(knopka6)
    keyboard.add(knopka7)

    send = bot.send_message(message.chat.id, 'Қажет тілді таңдаңыз!' 
                                             '\nВыберите нужный язык!', parse_mode='Markdown',
                            reply_markup=keyboard)
    bot.register_next_step_handler(send, eki)

def eki(message):
    # bot.send_message(chat_id=chat_id, text=message.text)

    if message.text == knopka6:

        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(knopka1)
        keyboard.add(knopka2)
        keyboard.add(knopka3)
        keyboard.add(knopka4)
        keyboard.add(knopka5)
        send = bot.send_message(message.chat.id,
                                'Қазақ тілі таңдалды.'
                                '\nЕнді Қажет құрылымды таңдаңыз!',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, second)

    elif message.text == knopka7:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add(knopka8)
        keyboard.add(knopka9)
        keyboard.add(knopka10)
        keyboard.add(knopka11)
        keyboard.add(knopka12)
        send = bot.send_message(message.chat.id,
                                'Выбран русский язык.'
                                '\nТеперь можете выбрать нужное подразделение!',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, dva)

    else:
        send = bot.send_message(message.chat.id, 'Нажмите на нужную кнопку')
        bot.register_next_step_handler(send, eki)

def first(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.add(knopka1)
    keyboard.add(knopka2)
    keyboard.add(knopka3)
    keyboard.add(knopka4)
    keyboard.add(knopka5)

    send = bot.send_message(message.chat.id, 'Қажет құрылымды таңдаңыз!', parse_mode='Markdown',
                            reply_markup=keyboard)
    bot.register_next_step_handler(send, second)


def second(message):
    # bot.send_message(chat_id=chat_id, text=message.text)

    if message.text == knopka1:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka1)
        bot.send_message(chat_id=1111510132, text=knopka1)
        send = bot.send_message(message.chat.id,
                                'Келесі ақпаратты толтыруыңызды сұраймыз: Аты-жөніңізді, байланыс контактіңізді, лауазымыңызды және қабылдауға жазылу уақытыңызды(күні мен сағаты,  бір тәулік бұрын жазылыңыз)',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka2:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka2)
        bot.send_message(chat_id=1111510132, text=knopka2)
        send = bot.send_message(message.chat.id,
                                'Келесі ақпаратты толтыруыңызды сұраймыз: Аты-жөніңізді, байланыс контактіңізді, лауазымыңызды және қабылдауға жазылу уақытыңызды(күні мен сағаты,  бір тәулік бұрын жазылыңыз)',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka3:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka3)
        bot.send_message(chat_id=1111510132, text=knopka3)
        send = bot.send_message(message.chat.id,
                                'Келесі ақпаратты толтыруыңызды сұраймыз: Аты-жөніңізді, байланыс контактіңізді, лауазымыңызды және қабылдауға жазылу уақытыңызды(күні мен сағаты,  бір тәулік бұрын жазылыңыз)',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka4:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka4)
        bot.send_message(chat_id=1111510132, text=knopka4)
        send = bot.send_message(message.chat.id,
                                'Келесі ақпаратты толтыруыңызды сұраймыз: Аты-жөніңізді, байланыс контактіңізді, лауазымыңызды және қабылдауға жазылу уақытыңызды(күні мен сағаты,  бір тәулік бұрын жазылыңыз)',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka5:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka5)
        bot.send_message(chat_id=1111510132, text=knopka5)
        send = bot.send_message(message.chat.id,
                                'Келесі ақпаратты толтыруыңызды сұраймыз: Аты-жөніңізді, байланыс контактіңізді, лауазымыңызды және қабылдауға жазылу уақытыңызды(күні мен сағаты,  бір тәулік бұрын жазылыңыз)',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    else:
        send = bot.send_message(message.chat.id, 'Төменде орналасқан батырманы басыңыз')
        bot.register_next_step_handler(send, second)



def odin(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.add(knopka8)
    keyboard.add(knopka9)
    keyboard.add(knopka10)
    keyboard.add(knopka11)
    keyboard.add(knopka12)

    send = bot.send_message(message.chat.id, 'Выберите нужное Вам подразделение!', parse_mode='Markdown',
                            reply_markup=keyboard)
    bot.register_next_step_handler(send, dva)


def dva(message):
    # bot.send_message(chat_id=chat_id, text=message.text)

    if message.text == knopka8:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka8)
        bot.send_message(chat_id=1111510132, text=knopka8)
        send = bot.send_message(message.chat.id,
                                'Просим оставить информацию: Ваше ФИО,контактные данные, должность(студент или сотрудник), дату и время встречи  записывайтесь на день раньше',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka9:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka9)
        bot.send_message(chat_id=1111510132, text=knopka9)
        send = bot.send_message(message.chat.id,
                                'Просим оставить информацию: Ваше ФИО,контактные данные, должность(студент или сотрудник), дату и время встречи  записывайтесь на день раньше',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka10:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka10)
        bot.send_message(chat_id=1111510132, text=knopka10)
        send = bot.send_message(message.chat.id,
                                'Просим оставить информацию: Ваше ФИО,контактные данные, должность(студент или сотрудник), дату и время встречи  записывайтесь на день раньше',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka11:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka11)
        bot.send_message(chat_id=1111510132, text=knopka11)
        send = bot.send_message(message.chat.id,
                                'Просим оставить информацию: Ваше ФИО,контактные данные, должность(студент или сотрудник), дату и время встречи  записывайтесь на день раньше',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    elif message.text == knopka12:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.add("/start")
        bot.send_message(chat_id=609240271, text=knopka12)
        bot.send_message(chat_id=1111510132, text=knopka12)
        send = bot.send_message(message.chat.id,
                                'Просим оставить информацию: Ваше ФИО,контактные данные, должность(студент или сотрудник), дату и время встречи  записывайтесь на день раньше',
                                parse_mode='Markdown', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

    else:
        send = bot.send_message(message.chat.id, 'Нажмите кнопку пожалуйста!')
        bot.register_next_step_handler(send, dva)


def third(message):
    bot.send_message(chat_id=609240271, text=message.text)
    bot.send_message(chat_id=1111510132, text=message.text)

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
