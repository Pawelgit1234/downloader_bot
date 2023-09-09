from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.bot import Bot

from pytube import Playlist
import shutil
import requests
import os

from ...states import YoutubeStates
from ...utils import sanitize_filename
from ...keyboards import youtube_playlist_menu_buttons


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