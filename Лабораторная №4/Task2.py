# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
      # TODO считать содержимое csv файла
def task(INPUT_FILENAME, OUTPUT_FILENAME, delimiter=","):
    with open(INPUT_FILENAME, 'r', newline='') as file:
        stro = csv.DictReader(file, delimiter=delimiter)
        data = [dict(i) for i in stro]
    with open(OUTPUT_FILENAME, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
