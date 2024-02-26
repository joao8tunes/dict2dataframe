#!/usr/bin/env python
# encoding: utf-8

# João Antunes <joao8tunes@gmail.com>
# https://github.com/joao8tunes

import json

from dict2dataframe.settings import setup_logger
from dict2dataframe.handlers import Dict

setup_logger(__name__)


def main() -> None:
    filepath = "samples/data/data.json"

    with open(filepath, mode="rt", encoding="utf-8") as file:
        data = json.load(file)
        d = Dict(data=data['values'][0])

    keys = ["b", "x"]
    value, value_exists = d.get(keys=keys)

    print(f"{keys} --> {value}") if value_exists else print(f"Key '{keys}' does not exists!")

    d.set(keys=keys, value=11)
    value, value_exists = d.get(keys=keys)

    print(f"{keys} --> {value}") if value_exists else print(f"Key '{keys}' does not exists!")

    keys = ["b", "z"]
    d.add(keys=keys, value=12)
    value, value_exists = d.get(keys=keys)

    print(f"{keys} --> {value}") if value_exists else print(f"Key '{keys}' does not exists!")

    keys = ["b", "y"]
    d.remove(keys=keys)
    value, value_exists = d.get(keys=keys)

    print(f"{keys} --> {value}") if value_exists else print(f"Key '{keys}' does not exists!")

    print(f"Data: {d.data}")
    print(f"Items: {list(d.items())}")


if __name__ == '__main__':
    main()
