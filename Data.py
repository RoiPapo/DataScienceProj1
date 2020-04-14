import pandas as pd
import math


def load_data(path, features):
    df = pd.read_csv(path)
    data = df.to_dict(orient="list")
    filtered_data = {k: data[k] for k in features}  # construct dict only with the features we have
    filtered_data["earnings"] = (list((map(lambda x: math.log10(x), filtered_data["earnings"]))))  # normalizatoin
    return filtered_data


def filter_by_features(data, feature, vlaues):
    list_of_wanted_indexes = []
    dict_of_fitting_values = {}
    l1 = []
    for index, elem in enumerate(data[feature]):
        if elem in vlaues:
            list_of_wanted_indexes.append(index)

    for key, value in data.items():
        for i in reversed(list_of_wanted_indexes):
            dict_of_fitting_values.setdefault(key, []).append(value.pop(i))

    return dict_of_fitting_values, data # the second includes no fitting items
