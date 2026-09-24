import pandas as pd

data = pd.read_csv("data.csv")


def get_data_panda():
    return data.to_dict(orient="records")
