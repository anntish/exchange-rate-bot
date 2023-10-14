from loader import bot
from utils.create_save_user import save_user_request
from utils.parse_min_max import parse_value


@bot.message_handler(commands=['high'])
def handler_high(message):
    """
    Обработчик сообщений для получения максимального курса к рублю.

    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request_text = message.text

    greatest = parse_value(max)

    greatest_name = greatest[0]
    greatest_value = greatest[1]

    response_text = f'Максимальный курс сейчас у {greatest_name} и составляет {greatest_value} руб.'

    save_user_request(user_id, request_text, response_text, message)