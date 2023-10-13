import requests
import bs4 as bs
from utils.api_date import current_api


def parse_rate(currency):
    data = requests.get(current_api)
    total_values = bs.BeautifulSoup(data.content, 'xml')

    currency_to_find = currency
    rate_elem = total_values.find_all('Name', text=currency_to_find)

    for element in rate_elem:

        valute_element = element.find_parent('Valute')
        rate_element = float(valute_element.find('Value').text.replace(',', '.'))

        result = round(rate_element, 2)

        return result
