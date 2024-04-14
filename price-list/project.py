import csv
import os
import re
from tabulate import tabulate

class PriceMachine():

    def __init__(self):
        self.data = []
        self.name_length = 0

    def load_prices(self, directory):
        self.data = []
        for filename in os.listdir(directory):
            if filename.endswith('.csv') and 'price' in filename.lower():
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        product_name = None
                        price = None
                        weight = None
                        for name_colum in row:
                            if re.search(r'(название|продукт|товар|наименование)', name_colum, re.IGNORECASE):
                                product_name = row[name_colum].strip()
                            elif re.search(r'(цена|розница)', name_colum, re.IGNORECASE):
                                price = float(row[name_colum].replace(',', '.').strip())
                            elif re.search(r'(фасовка|масса|вес)', name_colum, re.IGNORECASE):
                                weight = float(row[name_colum].replace(',', '.').strip())

                        if product_name and price is not None and weight is not None:
                            self.data.append([filename, product_name, price, weight, round(price / weight, 2)])

    def search_product_price_weight(self, headers):
        results = []
        for row in self.data:
            if re.search(headers, row[1], re.IGNORECASE):
                results.append(row)
        return sorted(results, key=lambda x: x[2] / x[3])

    def search_text(self, text):
        results = self.search_product_price_weight(text)
        self.consol_results(results)
        html_filename = 'search_results.html'
        self.export_to_html(results, html_filename)
        print(f"Результаты поиска сохранены в файле: {html_filename}")
    def main_load(self, directory):
        self.load_prices(directory)

        while True:
            enter = input("Введите текст для поиска (или 'exit' для завершения): ")
            if enter.lower() == 'exit' or enter.lower() == 'учше':
                print("Работа завершена.")
                break
            self.search_text(enter)

    def consol_results(self, results):
        headers = ['№', 'Наименование', 'цена', 'вес', 'цена за кг.', 'файл']
        numbered_results = [[i + 1] + result[1:] + [result[0]] for i, result in enumerate(results)]
        print(tabulate(numbered_results, headers=headers, tablefmt='pipe'))


    def export_to_html(self, results, filename):
        headers = ['№', 'Наименование', 'цена', 'вес', 'цена за кг.', 'файл']
        numbered_results = [[i + 1] + result[1:] + [result[0]] for i, result in enumerate(results)]
        table = tabulate(numbered_results, headers=headers, tablefmt='html')
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(table)

if __name__ == "__main__":
    pm = PriceMachine()
    cur_directory = os.path.dirname(os.path.abspath(__file__))
    pm.main_load(cur_directory)
