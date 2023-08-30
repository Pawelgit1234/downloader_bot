from aiogram import types

from ..keyboards.reply import start_command_buttons


async def start_command(message: types.Message) -> None:
	await message.delete()
	await message.answer("Hi, with me you can download Videos, img, etc", reply_markup=start_command_buttons())