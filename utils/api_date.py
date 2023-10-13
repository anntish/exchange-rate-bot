from datetime import date

curr_date = str(date.today()).split('-')
curr_day, curr_month, curr_year = curr_date[2], curr_date[1], curr_date[0]

current_api = f'https://cbr.ru/scripts/XML_daily.asp?date_req={curr_day}/{curr_month}/{curr_year}'
