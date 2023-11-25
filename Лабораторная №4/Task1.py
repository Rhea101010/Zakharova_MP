# TODO решите задачу
import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME, 'r') as file:
        data = json.load(file)
    itogo = sum([item["score"] * item["weight"] for item in data])
    return round(itogo, 3)


print(task())
