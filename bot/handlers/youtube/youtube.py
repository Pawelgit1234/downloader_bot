from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.bot import Bot

from ...keyboards import youtube_menu_buttons
from ...states import YoutubeStates


async def youtube_menu(message: types.Message) -> None:
	await message.delete()
	await message.answer("Choose what you want to download", reply_markup=youtube_menu_buttons())


async def youtube_ask_for_link(callback_query: types.CallbackQuery) -> None:
	bot: Bot = callback_query.bot
	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
	await bot.send_message(callback_query.from_user.id, 'Please send the Link.')

	match callback_query.data:
		case 'video':
			await YoutubeStates.VIDEO_LINK.set()
		case 'shorts':
			await YoutubeStates.SHORTS_LINK.set()
		case 'playlist':
			await YoutubeStates.PLAYLIST_LINK.set()
		case 'community':
			await YoutubeStates.COMMUNITY_LINK.set()
