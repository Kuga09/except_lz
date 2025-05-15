import os
import pandas as pd

class DatasetProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.expected_columns = [
            'Участники гражданского оборота',
            'Тип операции',
            'Сумма операции',
            'Вид расчета',
            'Место оплаты',
            'Терминал оплаты',
            'Дата оплаты',
            'Время оплаты',
            'Результат операции',
            'Cash-back',
            'Сумма cash-back'
        ]

    def process(self):
        try:
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"Файл не найден: {self.filename}")

            df = pd.read_csv(self.filename)

            if df.empty:
                raise ValueError("Файл пустой")

            if list(df.columns) != self.expected_columns:
                raise ValueError(
                    f"Структура не соответствует. Ожидаемые столбцы: {self.expected_columns}, "
                    f"найдено: {list(df.columns)}"
                )

            print("Файл успешно обработан и соответствует требованиям.")
            return df

        except Exception as e:
            print(f"Ошибка: {str(e)}")



