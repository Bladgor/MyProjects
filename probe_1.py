import telebot
from telebot import types

bot = telebot.TeleBot('5562447993:AAHxkSOD7HsgYawjsfb_wSRI-e9li_xhE6s')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    item_button_good = types.KeyboardButton('Хорошо')
    item_button_bad = types.KeyboardButton('Плохо')
    markup = types.ReplyKeyboardMarkup()
    markup.row(item_button_good, item_button_bad)
    bot.send_message(message.from_user.id, 'Привет! Как дела?', reply_markup=markup)


@bot.message_handler(regexp='Хорошо')
def send_good(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.from_user.id, 'Ну и отлично!', reply_markup=markup)


@bot.message_handler(regexp='Плохо')
def send_good(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.from_user.id, 'Плохо, когда плохо(((', reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling(interval=1)
