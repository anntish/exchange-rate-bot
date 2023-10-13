from loader import bot
from models.base_model import User


@bot.message_handler(commands=['help'])
def handler_help(message):

    user_id = message.from_user.id
    request_text = message.text

    response_text = 'Спасибо, что заинтересовались Курс Ботом!\n' \
                    'Доступные функции:\n' \
                    '/low - валюта с наименьшим курсом к рублю\n' \
                    '/high - валюта с наибольшим курсом к рублю\n' \
                    '/history - посмотреть историю запросов\n' \
                    'Вскоре будут доступны функции:\n' \
                    '/custom - посмотреть динамику доллара'

    user = User.create(user_id=user_id, request_text=request_text, response_text=response_text)
    user.save()

    bot.send_message(message.chat.id, response_text)
