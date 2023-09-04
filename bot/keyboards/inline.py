from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def youtube_menu_buttons():
	imk = InlineKeyboardMarkup()
	btn1 = InlineKeyboardButton('Video', callback_data='video')
	btn2 = InlineKeyboardButton('Shorts', callback_data='shorts')
	btn3 = InlineKeyboardButton('Playlist', callback_data='playlist')
	btn4 = InlineKeyboardButton('Community', callback_data='community')

	imk.row(btn1, btn2)
	imk.row(btn3, btn4)
	return imk


def youtube_video_menu_buttons():
	imk = InlineKeyboardMarkup()
	btn1 = InlineKeyboardButton("Audio", callback_data="v_audio")
	btn2 = InlineKeyboardButton("Video", callback_data="v_video_and_audio")
	btn3 = InlineKeyboardButton("Video without Audio", callback_data="v_video_without_audio")
	btn4 = InlineKeyboardButton("Thumbnail", callback_data="v_thumbnail")

	imk.row(btn1, btn2)
	imk.row(btn3, btn4)
	return imk


def youtube_choose_video_quality_buttons(video_quality_list: set):
	imk = InlineKeyboardMarkup(row_width=2)
	for quality in video_quality_list:
		button = InlineKeyboardButton(text=quality, callback_data=f"quality_{quality}")
		imk.insert(button)
	return imk