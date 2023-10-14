from datetime import date, timedelta

curr_date = date.today()

previous_date = curr_date - timedelta(days=9)
dates = [previous_date + timedelta(days=i) for i in range(10)]

dates = [d.strftime('%d/%m/%Y') for d in dates]
curr_date_format = curr_date.strftime('%d/%m/%Y')

current_api = f'https://cbr.ru/scripts/XML_daily.asp?date_req={curr_date_format}'
