from keyboards.currency_buttons import get_keyboard
from loader import bot
from models.query_model import Query


@bot.message_handler(commands=['start'])
def handle_start(message):
    """
    Обработчик сообщения /start

    :param message: Объект, предоставляющий сообщение пользователя
    :return: None
    """
    user_id = message.from_user.id
    request_text = message.text

    response_text = "Мир Курса Валют приветствует вас! 🌍👋\n" \
                    "Чтобы узнать список доступных команд введите /help"

    markup = get_keyboard()

    user = Query.create(user_id=user_id, request_text=request_text, response_text=response_text)
    user.save()

    bot.send_message(message.chat.id, response_text, reply_markup=markup)


