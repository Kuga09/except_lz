# Импорт класса
from checking import DatasetProcessor


# Функция main
def main():
    processor = DatasetProcessor('test.csv')
    processor.process()


if __name__ == "__main__":
    main()
