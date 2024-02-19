#!/usr/bin/env python
# encoding: utf-8

# João Antunes <joao8tunes@gmail.com>
# https://github.com/joao8tunes

import pandas as pd
import json
import os

from json2table.settings import setup_logger
from json2table.handlers import JSON

setup_logger(__name__)


def main() -> None:
    data_dir = "samples/data"
    table_dir = "samples/"

    df_list = []

    for file_name in os.listdir(data_dir):
        filepath = os.path.join(data_dir, file_name)

        with open(filepath, mode="rt", encoding="utf-8") as file:
            data = json.load(file)
            df = JSON(data['values']).to_dataframe()
            df_list.append(df)

    df = pd.concat(df_list, ignore_index=True)

    table_filepath = os.path.join(table_dir, "table.csv")
    df.to_csv(table_filepath, index=False)

    # table_filepath = os.path.join(table_dir, "table.xlsx")
    # df.to_excel(table_filepath, index=False)


if __name__ == '__main__':
    main()
