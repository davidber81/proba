from selenium import webdriver
import bs4
from time import sleep
import pandas as pd
from datetime import datetime
import csv

def write_cmc_top() -> dict:
    """Парсит сайт coinmarketcap.com. Берет данные(наименование, капитализация) первых 100 криптовалют"""
    driver = webdriver.Chrome()
    driver.get('https://coinmarketcap.com/')
    driver.maximize_window()
    px = 0                              #эта часть кода отвечает за получения кода с сайта, на выходе остается обычный файл супа с которым можно работать
    for i in range(10):
        px += 1000
        driver.execute_script(f'window.scrollTo(0, {px})')
        sleep(0.1)


    html = driver.page_source
    driver.close()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody').find_all('tr')
    name_capitalization = {}
    data = []
    total_capitalization = 0
    for tr in table:
        all_td = list(tr.find_all('td'))
        name = all_td[2]
        name = name.find_all('p')[0].get_text()
        capitalization = all_td[7]
        capitalization = capitalization.find_all('span')[1].get_text()
        total_capitalization_num = int(float(capitalization.replace(',', '').replace('$', '')))  # Преобразуем в целое число
        total_capitalization += total_capitalization_num
        data.append({'Name': name, 'MC': total_capitalization_num})
        # Преобразуем data в датафрейм pandas и рассчитаем MP - Market percentage (процент рынка) по каждой крипте
        df = pd.DataFrame(data)
        df['MP'] = (df['MC'] / total_capitalization) * 100
        df['MP'] = df['MP'].round(0).astype(int).astype(str) + '%'
        df['MC'] = df['MC'].apply(lambda x: f'{x:,}')
        #
        # Выведем получившийся датафрейм в консоль
        print(df)

        # Сохраним DataFrame в CSV, используя пробел в качестве разделителя
        file_name = f'{datetime.now().hour}.{datetime.now().minute} {datetime.now().strftime("%d.%m.%Y")}.csv'
        df.to_csv(file_name, sep=' ', index=False, quoting=csv.QUOTE_NONNUMERIC)
        name_capitalization[name] = capitalization
    return name_capitalization

write_cmc_top()