import pandas as pd
import sys

from Data import *


def main(argv):
    path = 'hw1_sample_input.csv'
    features = ['age', 'earnings', 'hours', 'week', 'female']
    men_stats = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    women_stats = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    all_stats = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    data = load_data(path, features)
    all_dict = load_data(path, features)
    values = set([1])
    female_dict, male_dict = filter_by_features(data, 'female', values)


if __name__ == "__main__":
    main(sys.argv)
