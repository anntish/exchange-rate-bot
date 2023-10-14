import requests
import bs4 as bs
from utils.api_date import dates


def get_dollar_dynamics():
    """
    Функция для получения значений курса доллара за последние 10 дней с использованием API Центрального банка России.

    :return: Список значений курса доллара за последние 10 дней.
    """
    dollar_values = []

    for elem in dates:
        actual_api = f'https://cbr.ru/scripts/XML_daily.asp?date_req={elem}'
        data = requests.get(actual_api)
        soup = bs.BeautifulSoup(data.content, 'xml')
        all_values = soup.find_all('Name', string='Доллар США')

        for record in all_values:
            dollar = record.find_parent('Valute')
            dollar_rate = float(dollar.find('Value').text.replace(',', '.'))
            dollar_values.append(round(dollar_rate, 2))

    return dollar_values
