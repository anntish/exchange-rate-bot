from loader import bot
from models.base_model import User
from utils.parser import parse_value


@bot.message_handler(commands=['high'])
def handler_high(message):

    user_id = message.from_user.id
    request_text = message.text

    greatest = parse_value(max)

    greatest_name = greatest[0]
    greatest_value = greatest[1]

    response_text = f'Максимальный курс сейчас у {greatest_name} и составляет {greatest_value} руб.'

    user = User.create(user_id=user_id, request_text=request_text, response_text=response_text)
    user.save()

    bot.send_message(message.chat.id, response_text)
