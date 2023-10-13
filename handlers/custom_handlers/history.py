import sqlite3
from loader import bot
from models.base_model import User


@bot.message_handler(commands=['history'])
def handler_history(message):
    user_id = message.from_user.id
    request_text = message.text

    connect = sqlite3.connect("database.pw")
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM (SELECT * FROM user WHERE user_id = ? "
                   "AND request_text != '/history' "
                   "AND request_text != '/help' "
                   "ORDER BY id DESC LIMIT 10) ORDER BY id ASC", (user_id,))

    data = cursor.fetchall()

    response_text = ''

    for entry in data:
        response_text += f'Запрос: {entry[3]}\n' \
                         f'Ответ: {entry[4]}\n\n'

    bot.send_message(message.chat.id, response_text)

    user = User.create(user_id=user_id, request_text=request_text, response_text=response_text)
    user.save()
