import pandas as pd
import sys

from Data import *


def main(argv):
    path = 'hw1_sample_input.csv'
    features = ['age', 'earnings', 'hours', 'week', 'female']
    men_stats = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    women_stats = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    all_stats = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    load_data(path, features)


if __name__ == "__main__":
    main(sys.argv)
