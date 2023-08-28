from bot import start_telegram_bot
import dotenv
import logging

dotenv.load_dotenv('.env')


def main():
	start_telegram_bot()


if __name__ == '__main__':
	main()
