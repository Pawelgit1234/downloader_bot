from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

from .handlers.main import register_all_handlers


async def on_start(dp: Dispatcher) -> None:
	register_all_handlers(dp)


def start_telegram_bot() -> None:
	bot = Bot(token=os.environ['BOT_TOKEN'])
	dp = Dispatcher(bot, storage=MemoryStorage())
	executor.start_polling(dp, skip_updates=True, on_startup=on_start)
