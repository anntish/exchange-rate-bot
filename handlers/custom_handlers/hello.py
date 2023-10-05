from loader import bot
from models.user import User


@bot.message_handler(commands=['hello-world'])
def handle_hello_world(message):
    user_id = message.from_user.id
    request_text = message.text
    response_text = 'Пока вас не было, курс валют в мире изменился.\n' \
                    'Чтобы узнать список доступных команд введите /help'

    user = User.create(user_id=user_id, request_text=request_text, response_text=response_text)
    user.save()

    bot.reply_to(message, response_text)


@bot.message_handler(func=lambda message: message.text.lower() == 'привет' or message.text.lower() == 'здравствуйте')
def handle_privet(message):
    user_id = message.from_user.id
    request_text = message.text
    response_text = 'Приветствую вас 👋\n' \
                    'Чтобы узнать список доступных команд введите /help'

    user = User.create(user_id=user_id, request_text=request_text, response_text=response_text)
    user.save()

    bot.reply_to(message, response_text)
