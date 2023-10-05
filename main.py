from loader import bot

from handlers.default_handlers import start, help
from handlers.custom_handlers import hello, unknown_handler


if __name__ == "__main__":

    bot.infinity_polling()

    bot.add_message_handler(start.handle_start)
    bot.add_message_handler(help.handler_help)
    bot.add_message_handler(hello.handle_hello_world)
    bot.add_message_handler(unknown_handler.unknown_input)

