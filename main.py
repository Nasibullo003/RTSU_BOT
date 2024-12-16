import telebot
from config import bot
from login_utils import *

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	msg = bot.reply_to(message, "Введите ваш логин", reply_markup=telebot.types.ReplyKeyboardRemove())
	bot.register_next_step_handler(msg, get_username)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()