import yfinance as yf

def fetch_stock_data(ticker: str, period: str):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    print(data)
    return data

def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data, ticker):
    avr_price = data['Close'].mean()
    avr_price_rounded = round(avr_price, 6)

    start_date = data.index.min().strftime('%Y-%m-%d')
    end_date = data.index.max().strftime('%Y-%m-%d')

    print(f'\nСредняя цена закрытия акции "{ticker}" за период <{start_date}...{end_date}> '
        f'составила: {avr_price_rounded}')

def export_data_to_csv(data, filename):
    data.to_csv(filename)
    print(f"\nДанные по запросу сохранены в файл {filename}")
