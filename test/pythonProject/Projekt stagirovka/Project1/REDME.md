# Документация проекта для анализа и визуализации данных об акциях

## Общий обзор

Этот проект предназначен для загрузки исторических данных об акциях и их визуализации. Он использует библиотеку yfinance
для получения данных и matplotlib для создания графиков. Пользователи могут выбирать различные тикеры и временные
периоды для анализа, а также просматривать движение цен и скользящие средние на графике

### 1. main.py:

- Является точкой входа в программу.

- Запрашивает у пользователя тикер акции и временной период, загружает данные, обрабатывает их и выводит результаты в
  виде графиков, а также записывает данные в CSV файл.

### 2. data_download.py:

- Отвечает за загрузку данных об акциях.

- Содержит функции для извлечения данных об акциях из интернета, расчёта:
    - средней цены закрытия акций за заданный период,
    - стандартного отклонения цены закрытия акций,
    - вывода уведомления о сильных колебаниях цены акции,
    - записи данных в CSV файл,
    - расчета дополнительных технических индикаторов (RSI, MACD)

### 3. data_plotting.py:

- Отвечает за визуализацию данных.

- Содержит функции для создания, сохранения и отображения в браузере графиков цены закрытия.

## Описание функций

### 1. main.py:

- main(): Основная функция, управляющая процессом загрузки, обработки данных и их визуализации. Запрашивает у
  пользователя ввод данных, вызывает функции загрузки и обработки данных, а затем передаёт результаты на визуализацию и
  выводит в консоль среднюю цену закрытия акций за заданный период, а также записывает данные в CSV файл.

### 2. data_download.py:

- fetch_stock_data(ticker, period): Получает исторические данные об акциях для указанного тикера и временного периода.
  Возвращает DataFrame с данными.

- add_moving_average(data, window_size): Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен
  закрытия.

- def calculate_and_display_average_price(data, ticker): Функция вычисляет и выводит в консоль среднюю цену закрытия
  акций за заданный период.

- def notify_if_strong_fluctuations(data, ticker, threshold=5): Функция вычисляет максимальное и минимальное значения
  цены закрытия и сравнивает с заданным порогом (по умолчанию порог threshold=5). Если разница превышает порог,
  пользователь получит уведомление.

- def export_data_to_csv(data, filename): Функция принимает DataFrame и имя файла, после чего сохраняет данные
  в указанный CSV файл.

- def calculate_rsi(data, window_size=14): Функция принимает DataFrame, кол-во наблюдений и вычисляет RSI.

- def calculate_macd(data, short_window=12, long_window=26, signal_window=9): Функция принимает DataFrame, значения окон
  и вычисляет MACD (Moving Average Convergence Divergence) и линию сигнала для заданных данных о цене закрытия акций.

### 3. data_plotting.py:

- def create_and_save_plot(data, ticker, period, start_date, end_date, std_deviation, style=None, filename=None):
  Функция создаёт график, отображающий цены закрытия, скользящие средние, дополнительные технические индикаторы (RSI, MACD,
  Стандартное отклонение).

## Пошаговое использование

1. Запустите main.py.

2. Введите интересующий вас тикер акции (например, 'AAPL' для Apple Inc).

3. Введите желаемый временной период для анализа (например, '1mo' для данных за один месяц), либо пропустите (enter) и
   укажите конкретные даты начала и окончания для анализа.
4. Выберите стиль графика (например, 'classic', 'ggplot', 'bmh', 'fivethirtyeight'), либо пропустите (enter) и график
   будет выбран стандартный по умолчанию

5. Программа обработает введённые данные, загрузит соответствующие данные об акциях, рассчитает скользящее среднее,
   дополнительные технические индикаторы (RSI, MACD) и отобразит графики, а также запишет дынные в CSV файл.

# Тесты

Модуль test_data_download.py содержит набор тестов для проверки функциональности функций, связанных с загрузкой данных о
ценных бумагах и их обработкой.