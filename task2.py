import csv
import json


INPUT_FILENAME = "input.csv"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        data_list = [line for line in csv.DictReader(f)]
    print(json.dumps(data_list, indent=4), end="")


if __name__ == '__main__':
    # Нужно для проверки
    task()