import os.path
import string

import pandas as pd


def to_csv(data: dict, path: string):
    if not os.path.exists(path):
        os.makedirs(path)
    for k, v in data.items():
        pd.DataFrame(v).to_csv(os.path.join(path, k + ".csv"))
