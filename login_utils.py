import telebot
from config import bot

def get_username(message):
	login = message.text
	msg = bot.reply_to(message, '🔒 Введите пароль восстановления', reply_markup=telebot.types.ReplyKeyboardRemove())
	bot.register_next_step_handler(msg, lambda message: get_password(message, login))

def get_password(message, login):
	password = message.text

	main_menu_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	main_menu_markup.row_width = 2

	menu_namespace_arr = ['✅Да', '❌Нет']
	main_menu_markup.add(*[telebot.types.KeyboardButton(i) for i in menu_namespace_arr])
	msg = bot.reply_to(message, f"{login=}, {password=}; верно ?", reply_markup=main_menu_markup)
	bot.register_next_step_handler(msg, lambda message: check_login(message, login, password))

def check_login(message, login, password):
	if message.text == '❌Нет':
		msg = bot.reply_to(message, "Введите ваш логин", reply_markup=telebot.types.ReplyKeyboardRemove())
		bot.register_next_step_handler(msg, get_username)
		return
	
	msg = bot.reply_to(message, "Loading")
