from aiogram.bot import Bot

import re
import os
import zipfile

from aiogram.dispatcher import FSMContext


def sanitize_filename(filename: str) -> str:
	sanitized_filename = re.sub(r'[\/:*?"<>|]', '_', filename)
	return sanitized_filename


async def upload_file(path: str, callback_query, file_type: str) -> None:
	bot: Bot = callback_query.bot

	with open(path, 'rb') as file:
		match file_type:
			case 'zip':
				await bot.send_document(callback_query.from_user.id, file)
			case 'audio':
				await bot.send_audio(callback_query.from_user.id, file)
			case 'video':
				await bot.send_video(callback_query.from_user.id, file)
			case _:
				raise Exception(f'Type ({file_type}) was not found.')


def create_zip(zip_path: str, files_path: str) -> None:
	with zipfile.ZipFile(zip_path, 'w') as zipf:
		for root, dirs, files in os.walk(files_path):
			for file in files:
				fpath = os.path.join(root, file)
				arcname = os.path.relpath(fpath, files_path)
				zipf.write(fpath, arcname=arcname)
