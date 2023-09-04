from aiogram.dispatcher.filters.state import StatesGroup, State


class YoutubeStates(StatesGroup):
	VIDEO_LINK = State()
	SHORTS_LINK = State()
	PLAYLIST_LINK = State()
	COMMUNITY_LINK = State()