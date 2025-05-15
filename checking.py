# Импорт используемых библиотек
import os
import pandas as pd


# Класс, обрабатывающий датафрейм
class DatasetProcessor:

    # Конструктор
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
        self.expected_dtypes = {
            'Участники гражданского оборота': 'object',
            'Тип операции': 'object',
            'Сумма операции': 'float64',
            'Вид расчета': 'object',
            'Место оплаты': 'object',
            'Терминал оплаты': 'object',
            'Дата оплаты': 'object',  
            'Время оплаты': 'object',
            'Результат операции': 'object',
            'Cash-back': 'object',
            'Сумма cash-back': 'float64'
        }
    
    # Функция, проверяющая файл
    def process(self):
        try:
            # Проверка файла на существование
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"Файл не найден: {self.filename}")

            df = pd.read_csv(self.filename)

            # Проверка файла на "пустоту"
            if df.empty:
                raise ValueError("Файл пустой")

             # Проверка структуры файла 
            if list(df.columns) != self.expected_columns:
                raise ValueError(
                    f"Структура не соответствует. Ожидаемые столбцы: {self.expected_columns}, "
                    f"найдено: {list(df.columns)}"
                )
            
            # Проверка типов данных
            mismatched_types = []
            for col, expected_type in self.expected_dtypes.items():
                actual_type = str(df[col].dtype)
                if actual_type != expected_type:
                    mismatched_types.append((col, expected_type, actual_type))

            if mismatched_types:
                error_msgs = [f"Столбец '{col}': ожидался тип {exp}, найден {act}"
                              for col, exp, act in mismatched_types]
                raise TypeError("Несоответствие типов данных:\n" + "\n".join(error_msgs))

            print("Файл успешно обработан.")
            return df

        except Exception as e:
            print(f"Ошибка: {str(e)}")



