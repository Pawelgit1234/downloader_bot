from aiogram import Dispatcher

from .youtube import register_youtube_handlers
from .commands import start_command


def register_all_handlers(dp: Dispatcher) -> None:
	register_youtube_handlers(dp)

	dp.register_message_handler(start_command, commands=['start'])
