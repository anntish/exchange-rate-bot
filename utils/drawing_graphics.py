import io
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from utils.api_date import dates
from utils.parse_dollar_dynamics import get_dollar_dynamics

matplotlib.use('Agg')


def create_graphics():
    """
    Создает график, отражающий динамику изменения курса доллара за последние 10 дней.

    :return: Байты, формирующие изображение
    """
    dollar_values = get_dollar_dynamics()

    df = pd.DataFrame({'days': dates, 'dollars': dollar_values})

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df['days'], df['dollars'])
    ax.set_xlabel('Дата')
    ax.set_ylabel('Курс доллара, руб.')
    ax.set_title('Изменение курса доллара за последние 10 дней')

    img_byte_io = io.BytesIO()
    fig.savefig(img_byte_io, format='png')

    img_byte_io.seek(0)
    plt.close(fig)

    return img_byte_io
