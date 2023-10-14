from telebot import types


def get_keyboard():
    """
    Создает и возвращает объект клавиатуры с кнопками.
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    btn1 = types.KeyboardButton('Доллар')
    btn2 = types.KeyboardButton('Евро')
    btn3 = types.KeyboardButton('Тенге')
    btn4 = types.KeyboardButton('Турецкая лира')
    btn5 = types.KeyboardButton('Грузинский лари')
    btn6 = types.KeyboardButton('Юань')
    btn7 = types.KeyboardButton('Драм')
    btn8 = types.KeyboardButton('Злотый')
    btn9 = types.KeyboardButton('Чешский крон')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

    return markup
