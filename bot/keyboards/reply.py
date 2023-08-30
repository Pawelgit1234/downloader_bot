from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_command_buttons():
	mk = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = KeyboardButton('🎥 Youtube 🎥')
	btn2 = KeyboardButton('🏷 Instagram 🏷')
	btn3 = KeyboardButton('🎤 TikTok 🎤')
	mk.row(btn1, btn2)
	mk.add(btn3)
	return mk
