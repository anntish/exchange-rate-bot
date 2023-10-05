from loader import bot
from models.base_model import User


@bot.message_handler(func=lambda message: True)
def unknown_input(message):

    user_id = message.from_user.id
    request_text = message.text

    response_text = 'Извините, я не понимаю вас. Для подробной информации о моих возможностях введите /help'

    user = User.create(user_id=user_id, request_text=request_text, response_text=response_text)
    user.save()

    bot.send_message(message.chat.id, response_text)
