import pandas as pd
import sys

from Data import *


def main(argv):
    men_stats = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    women_stats = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    all_stats = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    load_data("cat", "food")


if __name__ == "__main__":
    main(sys.argv)
