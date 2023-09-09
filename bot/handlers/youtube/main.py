from aiogram import Dispatcher

from .youtube import youtube_menu, youtube_ask_for_link
from .video import youtube_video_menu, youtube_choose_video_quality, youtube_video_download_callback, youtube_audio_download_callback, youtube_thumbnail_download_callback
from .playlist import youtube_playlist_menu
from ...states import YoutubeStates


def register_youtube_handlers(dp: Dispatcher) -> None:
	# register message handlers
	dp.register_message_handler(youtube_menu, lambda message: message.text == '🎥 Youtube 🎥')
	dp.register_message_handler(youtube_video_menu, lambda message: message.text.startswith('https://www.youtube.com/watch?v=') or message.text.startswith('https://youtu.be/') or message.text.startswith('https://youtube.com/shorts/') or message.text.startswith('https://www.youtube.com/shorts/'), state=YoutubeStates.VIDEO_LINK)
	dp.register_message_handler(youtube_playlist_menu, lambda message: message.text.startswith('https://youtube.com/playlist?list=') or message.text.startswith('https://www.youtube.com/playlist?list='), state=YoutubeStates.PLAYLIST_LINK)

	# register callback handlers
	dp.register_callback_query_handler(youtube_ask_for_link, lambda callback_query: callback_query.data in ('video', 'playlist', 'shorts', 'community'))
	dp.register_callback_query_handler(youtube_choose_video_quality, lambda callback_query: callback_query.data == 'v_video_and_audio', state='*')
	dp.register_callback_query_handler(youtube_video_download_callback, lambda callback_query: callback_query.data.startswith('quality_'), state='*')
	dp.register_callback_query_handler(youtube_audio_download_callback, lambda callback_query: callback_query.data == 'v_audio', state='*')
	dp.register_callback_query_handler(youtube_thumbnail_download_callback, lambda callback_query: callback_query.data == 'v_thumbnail', state='*')