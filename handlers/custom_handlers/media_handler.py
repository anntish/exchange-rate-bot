from loader import bot
from utils.create_save_user import save_user_request


@bot.message_handler(content_types=['photo', 'sticker', 'video', 'animation', 'voice'])
def handle_media(message):
    """
    Обработчик сообщений, содержащих медиа-элементы.

    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request = message.content_type

    if message.content_type == 'voice':
        response_text = '🐣Я еще слишком юн, чтобы понимать вашу речь.🐣\n' \
                        'Чтобы узнать о том, что я могу сейчас, введите /help'

    else:
        response_text = 'Теперь я чуть больше знаю о вашем визуальном вкусе 🗿\n' \
                        'Чтобы узнать о том, что я могу сейчас, введите /help'

    save_user_request(user_id, request, response_text, message)

