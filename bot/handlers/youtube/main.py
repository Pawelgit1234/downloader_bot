from aiogram import Dispatcher

from .youtube import youtube_menu, youtube_ask_for_link
from .video import youtube_video_menu, youtube_choose_video_quality, youtube_video_download_callback, youtube_audio_download_callback
from ...states import YoutubeStates


def register_youtube_handlers(dp: Dispatcher) -> None:
	# register message handlers
	dp.register_message_handler(youtube_menu, lambda message: message.text == '🎥 Youtube 🎥')
	dp.register_message_handler(youtube_video_menu,
		lambda message: 'https://www.youtube.com/watch?v=' in message.text or 'https://youtu.be/' in message.text,
		state=YoutubeStates.VIDEO_LINK)

	# register callback handlers
	dp.register_callback_query_handler(youtube_ask_for_link, lambda callback_query: callback_query.data in ('video', 'playlist', 'shorts', 'community'))
	dp.register_callback_query_handler(youtube_choose_video_quality, lambda callback_query: callback_query.data == 'v_video_and_audio', state='*')
	dp.register_callback_query_handler(youtube_video_download_callback, lambda callback_query: callback_query.data.startswith('quality_'), state='*')
	dp.register_callback_query_handler(youtube_audio_download_callback, lambda callback_query: callback_query.data == 'v_audio', state='*')