from loader import bot
from models.base_model import User
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
    user_id = message.from_user.id
    request_text = message.text

    if request_text in currency_dict:

        currency_name = currency_dict[message.text]
        rate = parse_rate(currency_name)

        response_text = f'Курс {message.text} составляет: {rate} руб.'
        bot.send_message(message.chat.id, response_text)

        user = User.create(user_id=user_id, request_text=request_text, response_text=response_text)
        user.save()

    else:
        response_text = 'Извините, я не понимаю вас. Для подробной информации о моих возможностях введите /help'
        bot.send_message(message.chat.id, response_text)

        user = User.create(user_id=user_id, request_text=request_text, response_text=response_text)
        user.save()

