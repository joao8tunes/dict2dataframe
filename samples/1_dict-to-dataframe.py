#!/usr/bin/env python
# encoding: utf-8

# João Antunes <joao8tunes@gmail.com>
# https://github.com/joao8tunes

import pandas as pd
import json
import os

from dict2dataframe.settings import setup_logger
from dict2dataframe.core import dict2dataframe

setup_logger(__name__)


def main() -> None:
    data_dir = "samples/data"
    table_dir = "samples/"

    df_list = []

    # Converting list of dict to table:
    for file_name in os.listdir(data_dir):
        filepath = os.path.join(data_dir, file_name)

        with open(filepath, mode="rt", encoding="utf-8") as file:
            data = json.load(file)
            df = dict2dataframe(data['values'])
            df_list.append(df)

    df = pd.concat(df_list, ignore_index=True)

    table_filepath = os.path.join(table_dir, "table.csv")
    df.to_csv(table_filepath, index=False)

    # table_filepath = os.path.join(table_dir, "table.xlsx")
    # df.to_excel(table_filepath, index=False)

    print(df)


if __name__ == '__main__':
    main()
