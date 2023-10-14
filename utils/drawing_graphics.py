import io
import pandas as pd
import matplotlib.pyplot as plt
from utils.api_date import dates
from utils.dollar_dynamics import get_dollar_dynamics


def create_graphics():
    dollar_values = get_dollar_dynamics()

    df = pd.DataFrame({'days': dates, 'dollars': dollar_values})

    plt.figure(figsize=(12, 6))

    plt.plot(df['days'], df['dollars'])
    plt.xlabel('Дата')
    plt.ylabel('Курс доллара, руб.')
    plt.title('Изменение курса доллара за последние 10 дней')

    img_byte_io = io.BytesIO()
    plt.savefig(img_byte_io, format='png')

    img_byte_io.seek(0)

    plt.close()

    return img_byte_io
