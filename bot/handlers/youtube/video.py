from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.bot import Bot

from pytube import YouTube
import shutil

from ...states import YoutubeStates
from ...keyboards import youtube_video_menu_buttons, youtube_choose_video_quality_buttons
from ...utils import youtube_video_quality_list


async def youtube_video_menu(message: types.Message, state: FSMContext):
	try:
		await message.delete()
		YouTube(message.text)
		async with state.proxy() as data:
			data['VIDEO_LINK'] = message.text

		await YoutubeStates.next()
		await message.answer('⬇️Choose what you want to download⬇️', reply_markup=youtube_video_menu_buttons())
	except:
		await message.answer("Please write a valid YouTube link.")


async def youtube_choose_video_quality(callback_query: types.CallbackQuery, state: FSMContext):
	bot: Bot = callback_query.bot
	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
	async with state.proxy() as data:
		link = data['VIDEO_LINK']

	quality_list = youtube_video_quality_list(link)
	await bot.send_message(callback_query.from_user.id, 'Choose quality', reply_markup=youtube_choose_video_quality_buttons(quality_list))


async def youtube_video_download_callback(callback_query: types.CallbackQuery, state: FSMContext):
	selected = callback_query.data.split('_')
	selected_quality = selected[1]

	bot: Bot = callback_query.bot
	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

	async with state.proxy() as data:
		link = data['VIDEO_LINK']

	try:
		yt = YouTube(link)
		stream = yt.streams.filter(res=selected_quality).first()
		if stream:
			video_path = f'bot/downloaded/youtube/video/{callback_query.from_user.id}'
			stream.download(output_path=video_path)
			with open(f'{video_path}/{yt.title}.mp4', 'rb') as video_file:
				await bot.send_video(callback_query.from_user.id, video_file)
			shutil.rmtree(video_path)
		else:
			await bot.send_message(callback_query.from_user.id, "Video could not be downloaded.")
	except:
		await bot.send_message(callback_query.from_user.id, f"Video could not be downloaded. Maybe it is to long.")
	finally:
		await state.finish()


async def youtube_audio_download_callback(callback_query: types.CallbackQuery, state: FSMContext):

	bot: Bot = callback_query.bot
	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

	async with state.proxy() as data:
		link = data['VIDEO_LINK']

	try:
		yt = YouTube(link)
		audio_stream = yt.streams.filter(only_audio=True).first()
		if audio_stream:
			video_path = f'bot/downloaded/youtube/video/{callback_query.from_user.id}'
			audio_stream.download(output_path=video_path)
			with open(f'{video_path}/{yt.title}.mp4', 'rb') as video_file:
				await bot.send_audio(callback_query.from_user.id, video_file)
			shutil.rmtree(video_path)
		else:
			await bot.send_message(callback_query.from_user.id, "Audio could not be downloaded.")
	except:
		await bot.send_message(callback_query.from_user.id, f"Audio could not be downloaded. Maybe it is to long.")
	finally:
		await state.finish()
