from loader import bot
from utils.create_save_user import save_user_request
from utils.parse_exchange_rates import parse_rate


currency_dict = {
    'Доллар': 'Доллар США',
    'Евро': 'Евро',
    'Тенге': 'Казахстанских тенге',
    'Турецкая лира': 'Турецких лир',
    'Грузинский лари': 'Грузинский лари',
    'Юань': 'Китайский юань',
    'Драм': 'Армянских драмов',
    'Злотый': 'Польский злотый',
    'Чешский крон': 'Чешских крон'
}


@bot.message_handler(content_types=['text'])
def get_value_rate(message):
    """
    Обработчик сообщений для получения курса по запрашиваемой пользователем валюте.

    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request_text = message.text

    if request_text in currency_dict:
        currency_name = currency_dict[message.text]
        rate = parse_rate(currency_name)

        response_text = f'Курс {message.text} составляет: {rate} руб.'

    else:
        response_text = 'Извините, я не понимаю вас. Для подробной информации о моих возможностях введите /help'

    save_user_request(user_id, request_text, response_text, message)

