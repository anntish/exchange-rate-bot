from loader import bot
from models.base_model import User


@bot.message_handler(content_types=['photo', 'sticker', 'video', 'animation', 'voice'])
def handle_media(message):
    user_id = message.from_user.id
    request = message.content_type

    if message.content_type == 'voice':
        response_text = '🐣Я еще слишком юн, чтобы понимать вашу речь.🐣\n' \
                        'Чтобы узнать о том, что я могу сейчас, введи /help'

        user = User.create(user_id=user_id, request_text=request, response_text=response_text)
        user.save()

        bot.send_message(message.chat.id, response_text)

    else:
        response_text = 'Теперь я чуть больше знаю о вашем визуальном вкусе 🗿\n' \
                        'Чтобы узнать о том, что я могу сейчас, введи /help'

        user = User.create(user_id=user_id, request_text=request, response_text=response_text)
        user.save()

        bot.send_message(message.chat.id, response_text)

