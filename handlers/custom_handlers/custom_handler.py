from loader import bot
from models.base_model import User
from utils.api_date import dates
from utils.drawing_graphics import create_graphics
from utils.dollar_dynamics import get_dollar_dynamics


@bot.message_handler(commands=['custom'])
def handler_dollar_dynamic(message):
    user_id = message.from_user.id
    request_text = message.text

    img_io = create_graphics()

    bot.send_photo(message.chat.id, img_io)

    dollar_values = get_dollar_dynamics()

    dollar_dynamics = list(zip(dates, dollar_values))

    response = 'Динамика курса доллара за последние 10 дней:\n\n'

    for date, rate in dollar_dynamics:
        response += f"{date}: {rate} руб.\n"

    bot.send_message(message.chat.id, response)
    user = User.create(user_id=user_id, request_text=request_text, response_text=response)
    user.save()
