import os
import matplotlib.pyplot as plt


def create_and_save_plot(data, ticker, period, start_date, end_date, filename=None):
    try:

        fig, axs = plt.subplots(3, 1, figsize=(18, 12))

        axs[0].plot(data.index, data['Close'], label='Цена закрытия', color='blue')
        axs[0].plot(data.index, data['Moving_Average'], label='Скользящее среднее', color='orange')
        axs[0].set_ylabel('Цена')
        axs[0].set_title(f"Цены акций {ticker} и скользящее среднее")

        plt.xlabel("Дата")

        if filename is None:
            filename = f"{ticker}_{period}_chart.png" if period else f"{ticker}_{start_date}_to_{end_date}_chart.png"

        plt.savefig(filename)
        print(f"Графики сохранены в {filename}")

        if os.path.exists(filename):
            print(f"Файл {filename} был успешно создан.")
        else:
            print(f"Ошибка: Файл {filename} не был создан.")
    except Exception as e:
        print(f"\nОшибка при создании и сохранении графика: {e}")