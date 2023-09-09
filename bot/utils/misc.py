import re


def sanitize_filename(filename: str) -> str:
	sanitized_filename = re.sub(r'[\/:*?"<>|]', '_', filename)
	return sanitized_filename
