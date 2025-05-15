from checking import DatasetProcessor


def main():
    processor = DatasetProcessor('test.csv')
    processor.process()


if __name__ == "__main__":
    main()
