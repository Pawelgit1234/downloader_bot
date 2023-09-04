from pytube import YouTube


def youtube_video_quality_list(link: str) -> set:
	yt = YouTube(link)
	videos = yt.streams.filter(file_extension='mp4', type='video')
	videos_types = set(f'{video.resolution}' for video in videos)
	return videos_types