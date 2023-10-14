from loader import bot
from utils.api_date import dates
from utils.create_save_user import save_user_request
from utils.drawing_graphics import create_graphics
from utils.parse_dollar_dynamics import get_dollar_dynamics


@bot.message_handler(commands=['custom'])
def handler_dollar_dynamic(message):
    """
    Обработчик сообщений для получения курса доллара за последние 10 дней.

    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request_text = message.text

    img_io = create_graphics()
    dollar_values = get_dollar_dynamics()
    dollar_dynamics = list(zip(dates, dollar_values))

    response_text = 'Динамика курса доллара за последние 10 дней:\n\n'

    for date, rate in dollar_dynamics:
        response_text += f"{date}: {rate} руб.\n"

    bot.send_photo(message.chat.id, img_io)

    save_user_request(user_id, request_text, response_text, message)
