import pandas as pd
import math

def load_data(path, features):
    path = 'hw1_sample_input.csv'
    df = pd.read_csv(path)
    data = df.to_dict(orient="list")
    keys_to_remove = ["race", "union", "uncov", "region", "hisp"]
    for key in keys_to_remove:
        del data[key]
    print(data["earnings"])



def filter_by_features(data, feature, vlaues):
    pass
