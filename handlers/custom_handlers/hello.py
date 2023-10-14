from loader import bot
from utils.create_save_user import save_user_request


@bot.message_handler(commands=['hello-world'])
def handle_hello_world(message):
    """
    Обработчик сообщения /hello-world

    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request_text = message.text

    response_text = 'Пока вас не было, курс валют в мире изменился.\n' \
                    'Чтобы узнать список доступных команд введите /help'

    save_user_request(user_id, request_text, response_text, message)


@bot.message_handler(func=lambda message: message.text.lower() == 'привет' or message.text.lower() == 'здравствуйте')
def handle_privet(message):
    """
    Обработчик сообщения 'привет' или 'здравствуйте' для отправки приветствия.

    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request_text = message.text

    response_text = 'Приветствую вас 👋\n' \
                    'Чтобы узнать список доступных команд введите /help'

    save_user_request(user_id, request_text, response_text, message)
