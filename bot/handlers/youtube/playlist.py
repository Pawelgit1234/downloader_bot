from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.bot import Bot

from pytube import Playlist, YouTube
import shutil
import os
import time

from ...states import YoutubeStates
from ...utils import sanitize_filename, upload_file, create_zip
from ...keyboards import youtube_playlist_menu_buttons, youtube_playlist_video_quality_buttons


async def youtube_playlist_menu(message: types.Message, state: FSMContext):
	try:
		await message.delete()
		Playlist(message.text)
		async with state.proxy() as data:
			data['PLAYLIST_LINK'] = message.text

		await YoutubeStates.next()
		await message.answer('⬇️Choose what you want to download⬇️', reply_markup=youtube_playlist_menu_buttons())
	except:
		await message.answer("Please write a valid Playlist link.")


async def youtube_playlist_audio_download_callback(callback_query: types.CallbackQuery, state: FSMContext):
	bot: Bot = callback_query.bot
	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

	async with state.proxy() as data:
		link = data['PLAYLIST_LINK']

	try:
		yt_playlist = Playlist(link)
		audio_path = f'bot/downloaded/youtube/playlist/{callback_query.from_user.id}'
		os.makedirs(audio_path, exist_ok=True)
		for audio_link in yt_playlist:
			yt = YouTube(audio_link)
			audio_stream = yt.streams.filter(only_audio=True).first()
			if audio_stream:
				yt_audio_title = sanitize_filename(yt.title)
				audio_stream.download(output_path=audio_path, filename=yt_audio_title + '.mp3')
			else:
				await bot.send_message(callback_query.from_user.id, "Audio could not be downloaded.")

		zip_path = 'bot/downloaded/youtube/playlist/zip/' + str(int(time.time())) + '.zip'
		create_zip(zip_path, audio_path)
		await upload_file(zip_path, callback_query, 'zip')

		shutil.rmtree(audio_path)
		os.remove(zip_path)
	except:
		await bot.send_message(callback_query.from_user.id, f"Playlist could not be downloaded. Maybe it is to long.")
	finally:
		await state.finish()


async def youtube_playlist_choose_quality(callback_query: types.CallbackQuery):
	bot: Bot = callback_query.bot
	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

	await bot.send_message(callback_query.from_user.id, 'Choose quality', reply_markup=youtube_playlist_video_quality_buttons())


async def youtube_playlist_video_download_callback(callback_query: types.CallbackQuery, state: FSMContext):
	global video_stream
	bot: Bot = callback_query.bot
	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
	res = callback_query.data.split('_')[-1]

	async with state.proxy() as data:
		link = data['PLAYLIST_LINK']

	try:
		yt_playlist = Playlist(link)
		video_path = f'bot/downloaded/youtube/playlist/{callback_query.from_user.id}'
		os.makedirs(video_path, exist_ok=True)
		for video_link in yt_playlist:
			yt = YouTube(video_link)

			match res:
				case 'low':
					video_stream = yt.streams.get_lowest_resolution()
				case 'high':
					video_stream = yt.streams.get_highest_resolution()

			if video_stream:
				yt_video_title = sanitize_filename(yt.title)
				video_stream.download(output_path=video_path, filename=yt_video_title + '.mp4')
			else:
				await bot.send_message(callback_query.from_user.id, "Video could not be downloaded.")

		zip_path = 'bot/downloaded/youtube/playlist/zip/' + str(int(time.time())) + '.zip'
		create_zip(zip_path, video_path)
		await upload_file(zip_path, callback_query, 'zip')

		shutil.rmtree(video_path)
		os.remove(zip_path)
	except:
		await bot.send_message(callback_query.from_user.id, f"Playlist could not be downloaded. Maybe it is to long.")
	finally:
		await state.finish()