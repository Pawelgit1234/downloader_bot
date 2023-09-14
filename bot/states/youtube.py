from aiogram.dispatcher.filters.state import StatesGroup, State


class YoutubeStates(StatesGroup):
	VIDEO_AND_SHORT_LINK = State()
	PLAYLIST_LINK = State()
	COMMUNITY_LINK = State()