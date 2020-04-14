import pandas as pd
import math


def load_data(path, features):
    """
    :param path: path to the file
    :param features: list of features
    :return: data after normalisation and choosing the interesting features
    """
    df = pd.read_csv(path)
    data = df.to_dict(orient="list")
    filtered_data = {k: data[k] for k in features}  # construct dict only with the features we have
    filtered_data["earnings"] = (list((map(lambda x: math.log10(x), filtered_data["earnings"]))))  # normalizatoin
    return filtered_data


def filter_by_features(data, feature, values):
    """
    :type values: set
    :type feature: list
    :type data: dict
    :return : 2 dicts one with the fitting condition and one without
    """
    list_of_wanted_indexes = []
    dict_of_fitting_values = {}
    l1 = []
    for index, elem in enumerate(data[feature]):
        if elem in values:
            list_of_wanted_indexes.append(index)

    for key, value in data.items():
        for i in reversed(list_of_wanted_indexes):
            dict_of_fitting_values.setdefault(key, []).append(value.pop(i))

    return dict_of_fitting_values, data # the second includes no fitting items
