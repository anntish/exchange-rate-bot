import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Отсутствует файл .env. Переменные окружения не могут быть загружены.')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')
