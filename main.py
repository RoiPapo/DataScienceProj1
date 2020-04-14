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
    s = set([1])
    filter_by_features(data, 'female', s)


if __name__ == "__main__":
    main(sys.argv)
