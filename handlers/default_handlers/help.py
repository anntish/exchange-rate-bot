from loader import bot


@bot.message_handler(commands=['help'])
def handler_help(message):
    response_text = 'Спасибо, что заинтересовались Курс Ботом!\n' \
                    'Вскоре будут доступны функции:\n' \
                    '/low - валюта с наименьшим курсом к рублю\n' \
                    '/high - валюта с наибольшим курсом к рублю\n' \
                    '/custom - посмотреть динамику доллара\n' \
                    '/history - посмотреть историю запросов'

    bot.send_message(message.chat.id, response_text)
