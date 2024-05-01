import os
import matplotlib.pyplot as plt

def create_and_save_plot(data, ticker, period, start_date, end_date, filename = None):
    """
    Создает и сохраняет интерактивный график на основе данных о биржевой акции.
    Параметры:
        data: Данные о биржевой акции в формате DataFrame.
        ticker: Тикер акции.
        period: Период для данных.
        start_date: Дата начала анализа.
        end_date: Дата окончания анализа.
        filename: Имя файла для сохранения графика. По умолчанию None.
    """
    try:

        fig, axs = plt.subplots(3, 1, figsize=(18, 25))

        # График цены закрытия, скользящего среднего и стандартного отклонения
        axs[0].plot(data.index, data['Close'], label='Цена закрытия', color='blue')
        axs[0].plot(data.index, data['Moving_Average'], label='Скользящее среднее', color='orange')
        fill_label = 'Стандартное отклонение'
        axs[0].fill_between(data.index, data['Close'] - data['Close'], color='lightblue',
                            alpha=0.5, label=fill_label)
        axs[0].set_ylabel('Цена')
        axs[0].set_title(f"\nЦены акций {ticker}, скользящее среднее и стандартное отклонение\n", fontweight='bold',
                         fontsize=16)
        axs[0].legend()

        # График RSI
        axs[1].plot(data.index, data['RSI'], label='RSI', color='purple')
        axs[1].axhline(70, color='r', linestyle='--')
        axs[1].axhline(30, color='g', linestyle='--')
        axs[1].set_ylabel('RSI')
        axs[1].set_title(f"\nОтносительный индекс силы {ticker} (RSI)\n", fontweight='bold',
                         fontsize=16)
        axs[1].legend()

        # График MACD
        axs[2].plot(data.index, data['MACD'], label='MACD', color='blue')
        axs[2].plot(data.index, data['Signal_Line'], label='Сигнальная линия', color='orange')
        axs[2].set_ylabel('MACD')
        axs[2].set_title(f"\nСхождение и расхождение скользящих средних {ticker} (MACD)\n", fontweight='bold',
                         fontsize=16)
        axs[2].legend()

        fig.suptitle(f"Анализ акций {ticker}", fontsize=20, fontweight='bold')  # Общий заголовок

        plt.xlabel("Дата")

        if filename is None:
            filename = f"{ticker}_{period}_chart.png" if period else f"{ticker}_{start_date}_to_{end_date}_chart.png"

        plt.savefig(filename)
        print(f"Графики сохранены в {filename}")

        # Проверка наличия файла
        if os.path.exists(filename):
            print(f"Файл {filename} был успешно создан.")
        else:
            print(f"Ошибка: Файл {filename} не был создан.")
    except Exception as e:
        print(f"\nОшибка при создании и сохранении графика: {e}")