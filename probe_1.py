import telebot

bot = telebot.TeleBot('5562447993:AAHxkSOD7HsgYawjsfb_wSRI-e9li_xhE6s')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Привет! Как дела?')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling(interval=1)
