import sqlite3
from loader import bot
from utils.create_save_user import save_user_request


@bot.message_handler(commands=['history'])
def handler_history(message):
    """
    Обработчик сообщений для получения истории последних 10 запросов пользователя.
    Не учитываются базовые запросы (/history, /help, /start)
    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request_text = message.text

    connect = sqlite3.connect("database.pw")
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM (SELECT * FROM query WHERE user_id = ? "
                   "AND request_text != '/history' "
                   "AND request_text != '/help' "
                   "AND request_text != '/start'"
                   "ORDER BY id DESC LIMIT 10) ORDER BY id ASC", (user_id,))

    data = cursor.fetchall()

    response_text = ''

    for entry in data:
        response_text += f'Запрос: {entry[3]}\n' \
                         f'Ответ: {entry[4]}\n\n'

    save_user_request(user_id, request_text, response_text, message)
