from aiogram import Dispatcher

from .youtube import register_youtube_handlers

from .youtube import youtube_menu


def register_all_handlers(dp: Dispatcher) -> None:
	register_youtube_handlers(dp)

	dp.register_message_handler(youtube_menu, commands=['start'])
