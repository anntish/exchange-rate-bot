from loader import bot
from models.base_model import User
from utils.parser import parse_value


@bot.message_handler(commands=['low'])
def handler_low(message):

    user_id = message.from_user.id
    request_text = message.text

    lower = parse_value(min)

    lower_name = lower[0]
    lower_value = lower[1]

    response_text = f'Минимальный курс сейчас у {lower_name} и составляет {lower_value} руб.'

    user = User.create(user_id=user_id, request_text=request_text, response_text=response_text)
    user.save()

    bot.send_message(message.chat.id, response_text)
