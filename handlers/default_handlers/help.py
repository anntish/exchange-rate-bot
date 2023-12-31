from loader import bot
from utils.create_save_user import save_user_request


@bot.message_handler(commands=['help'])
def handler_help(message):
    """
    Обработчик сообщения /help

    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request_text = message.text

    response_text = '👾Спасибо, что заинтересовались Курс Ботом!\n' \
                    'Доступные функции:\n' \
                    '/low - валюта с наименьшим курсом к рублю\n' \
                    '/high - валюта с наибольшим курсом к рублю\n' \
                    '/history - посмотреть историю запросов\n'\
                    '/custom - посмотреть динамику доллара\n'\
                    '💰Также вы можете узнать интересующие курсы валют через меню бота\n\n' \


    save_user_request(user_id, request_text, response_text, message)

