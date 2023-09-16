from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def youtube_menu_buttons():
	imk = InlineKeyboardMarkup()
	btn1 = InlineKeyboardButton('Video and Shorts', callback_data='video')
	btn2 = InlineKeyboardButton('Playlist', callback_data='playlist')

	imk.row(btn1, btn2)
	return imk


def youtube_video_menu_buttons():
	imk = InlineKeyboardMarkup()
	btn1 = InlineKeyboardButton("Audio", callback_data="v_audio")
	btn2 = InlineKeyboardButton("Video", callback_data="v_video_and_audio")
	btn3 = InlineKeyboardButton("Thumbnail", callback_data="v_thumbnail")

	imk.row(btn1, btn2)
	imk.add(btn3)
	return imk


def youtube_choose_video_quality_buttons(video_quality_list: set):
	imk = InlineKeyboardMarkup(row_width=2)
	for quality in video_quality_list:
		button = InlineKeyboardButton(text=quality, callback_data=f"quality_{quality}")
		imk.insert(button)
	return imk


def youtube_playlist_menu_buttons():
	imk = InlineKeyboardMarkup()
	btn1 = InlineKeyboardButton("Video", callback_data="p_video_and_audio")
	btn2 = InlineKeyboardButton("Audio", callback_data="p_audio")
	imk.add(btn1, btn2)

	return imk


def youtube_playlist_video_quality_buttons():
	imk = InlineKeyboardMarkup()
	btn1 = InlineKeyboardButton("High Quality", callback_data="p_quality_high")
	btn2 = InlineKeyboardButton("Low Quality", callback_data="p_quality_low")
	imk.add(btn1, btn2)

	return imk
