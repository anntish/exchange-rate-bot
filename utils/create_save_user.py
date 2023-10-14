from models.query_model import Query
from loader import bot


def save_user_request(user_id, request_text, response_text, message):
    """
    Сохраняет запрос пользователя, и отправляет ответ.

    Args:
        user_id (int): Индивидуальный идентификатор пользователя
        request_text (str): Текст запроса
        response_text (str): Текст ответа
        message (telegram.Message): Объект, предоставляющий сообщение пользователя

    :return: None
    """
    user = Query.create(user_id=user_id, request_text=request_text, response_text=response_text)
    user.save()
    bot.reply_to(message, response_text)

