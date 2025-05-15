import pandas as pd
import os


class Ex:
    @staticmethod
    def check():
        try:
            os.path.isfile("test.csv")
            df = fil
        except:
            print('Возникла следующая ошибка: Файл отсутствует в указанной директории.')
        else:
            try:
                if df.empty:
                    raise ValueError
            except:
                print('Возникла следующая ошибка: Датафрейм пуст')
            else:
                try:
                    expected_columns = ['Участники гражданского оборота', 'Тип операции', 'Сумма операции','Вид расчета','Место оплаты','Терминал оплаты','Дата оплаты','Время оплаты','Результат операции','Cash-back','Сумма cash-back'] 
                    for col in expected_columns:
                        if col not in list(df.columns): 
                            raise ValueError
                except:
                    print('Датафрейм НЕ соответствует ожидаемой структуре')
                else:
                    try:   
                        if list(df.columns) != expected_columns:
                            raise ValueError
                    except:
                        print('Датафрейм НЕ соответствует ожидаемой структуре')
                    else:
                        print('Чтение датафрейма завершено успешно.')

Ex.check()