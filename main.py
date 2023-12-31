from loader import bot

from handlers.default_handlers import start, help, history
from handlers.custom_handlers import hello, low, high, media_handler, custom_handler, currency_handlers


if __name__ == "__main__":
    bot.infinity_polling()

    bot.add_message_handler(start.handle_start)
    bot.add_message_handler(help.handler_help)
    bot.add_message_handler(hello.handle_hello_world)
    bot.add_message_handler(low.handler_low)
    bot.add_message_handler(high.handler_high)
    bot.add_message_handler(history.handler_history)
    bot.add_message_handler(media_handler.handle_media)
    bot.add_message_handler(custom_handler.handler_dollar_dynamic)
    bot.add_message_handler(currency_handlers.get_value_rate)



