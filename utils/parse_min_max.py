import requests
import bs4 as bs
from utils.api_date import current_api


def parse_value(action):
    """
    Функция для парсинга данных в формате XML с API Центрального банка России.
    Не учитываются значения 'СДР (специальные права заимствования)' т.к СДР - актив, а не валюта.

    :param action: Действие, которое необходимо выполнить в зависимости от запроса пользователя (min/max)
    :return: Список, содержащий Имя валюты и ее Значение
    """
    data = requests.get(current_api)
    total_values = bs.BeautifulSoup(data.content, 'xml')

    exchange_rate = total_values.find_all('Value')
    name = total_values.find_all('Name')
    num_codes = total_values.find_all('NumCode')

    currency_values = [float(value.text.replace(',', '.'))
                       for value, num_code in zip(exchange_rate, num_codes)
                       if num_code.text != '960']

    searched_currency = action(currency_values)

    value_index = currency_values.index(searched_currency)
    currency_name = name[value_index].text

    result_value = round(searched_currency, 2)

    result = [currency_name, result_value]

    return result


