import os.path
import string

import pandas as pd


def to_csv(data: dict, path: string, scoring='accuracy', param_opt=False):
    multi_score = not isinstance(scoring, str)
    if not os.path.exists(path):
        os.makedirs(path)
    if param_opt:
        pd.DataFrame(data['mean_fit_time']).to_csv(os.path.join(path, "mean_fit_time.csv"))
        pd.DataFrame(data['mean_score_time']).to_csv(os.path.join(path, "mean_score_time.csv"))
        for s in scoring:
            pd.DataFrame(data['mean_test_'+s]).to_csv(os.path.join(path, 'mean_test_'+s + ".csv"))
            pd.DataFrame(data['mean_train_'+s]).to_csv(os.path.join(path, 'mean_train_'+s + ".csv"))
    else:
        pd.DataFrame(data['fit_time']).to_csv(os.path.join(path, "mean_fit_time.csv"))
        pd.DataFrame(data['score_time']).to_csv(os.path.join(path, "mean_score_time.csv"))
        for s in scoring:
            pd.DataFrame(data['test_'+s]).to_csv(os.path.join(path, 'mean_test_'+s + ".csv"))
            pd.DataFrame(data['train_'+s]).to_csv(os.path.join(path, 'mean_train_'+s + ".csv"))