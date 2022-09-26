from oauth2client.service_account import ServiceAccountCredentials as sac
from datetime import datetime
from bs4 import BeautifulSoup as bs
import pandas as pd
import gspread
import requests


def get_data_from_sheet(sheet_name: str, sheet_num: int = 0) -> pd.DataFrame:
    """
    get_data_from_sheet получает данные из гугл таблицы

    Args:
        sheet_name (str): Имя гугл таблицы
        sheet_num (int): Номер листа таблицы

    Returns:
        pd.DataFrame: Дата фрейм с данными из гугл таблицы
    """
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials_path = 'token.json'

    credentials = sac.from_json_keyfile_name(credentials_path, scope)
    #
    client = gspread.authorize(credentials)
    # получаем данные из гугл таблице
    sheet = client.open(sheet_name).get_worksheet(
        sheet_num).get_all_records()
    return pd.DataFrame.from_dict(sheet)


def format_date_for_CB(date: str) -> str:
    """
    format_date форматирует дату формата ддммгггг в дату формата
    дд/мм/гггг

    Args:
        date (str): дата формата ддммгггг

    Returns:
        str: датf формата дд/мм/гггг
    """
    return date[:2] + '/' + date[2:4] + '/' + date[4:]


def format_date_for_Django(date: str) -> str:
    str_list = date.split('.')[::-1]
    return '-'.join(str_list)


def get_usd_course() -> float:
    """
    get_usd_course получает курс доллара от ЦБ РФ

    Returns:
        float: курс доллара
    """
    # текущая дата в формате ддммгггг
    current_date = datetime.now().strftime('%d%m%Y')
    # форматируем дату для корректного запроса
    request_date = format_date_for_CB(current_date)
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
    params = {'date_req': request_date}
    # делаем запрос на сайт ЦБ
    request = requests.get(url, params)
    # парсим данные из запроса
    soup = bs(request.content, 'xml')
    # находим курс доллара
    usd_course = soup.find(ID='R01235').Value.string
    return float(usd_course.replace(',', '.'))


def get_json_data():
    sheet_data = get_data_from_sheet('test_canalservice', 0)
    usd_course = get_usd_course()
    sheet_data['стоимость в руб.'] = sheet_data['стоимость,$'] * usd_course
    sheet_data = sheet_data[sheet_data.columns[[0, 1, 2, 4, 3]]]
    sheet_data.rename(columns={
        '№': 'id',
        'заказ №': 'number',
        'стоимость,$': 'price_usd',
        'стоимость в руб.': 'price_rub',
        'срок поставки': 'delivery_date'
    }, inplace=True)
    sheet_data['delivery_date'] = sheet_data['delivery_date'].apply(
        format_date_for_Django)
    return sheet_data.to_dict('records')


# test = get_json_data()
# print()
