import json


def save_dictionary(path, data_dict: dict):
    with open(path, 'w') as f:
        json.dump(data_dict, f)


def load_dictionary(path) -> dict:
    with open(path, 'r') as f:
        return json.load(f)
