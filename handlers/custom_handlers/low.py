from loader import bot
from utils.create_save_user import save_user_request
from utils.parse_min_max import parse_value


@bot.message_handler(commands=['low'])
def handler_low(message):
    """
    Обработчик сообщений для получения минимального курса к рублю.

    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request_text = message.text

    lower = parse_value(min)

    lower_name = lower[0]
    lower_value = lower[1]

    response_text = f'Минимальный курс сейчас у {lower_name} и составляет {lower_value} руб.'

    save_user_request(user_id, request_text, response_text, message)
