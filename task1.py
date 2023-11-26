import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)

    list_multiplication = [item["score"] * item["weight"] for item in json_data]
    return round(sum(list_multiplication), 3)


print(task())
