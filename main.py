import sys
from Data import *
from Statistics import sum2, median, mean, population_statistics


def main(argv):
    path = 'hw1_sample_input.csv'  # REMEMBER T0 CHANGE BEFORE HANDING
    features = ['age', 'female', 'education', 'earnings', 'hours', 'week', 'marital']
    features_of_part_a = ['age', 'earnings', 'hours', 'week']
    print("Question 1:")
    data = load_data(path, features)
    all_dict = load_data(path, features)
    values = set([1])
    female_dict, male_dict = filter_by_features(data, 'female', values)
    dict_list = [male_dict, female_dict, all_dict]
    population_list = ["Men", "Women", "All"]
    statistic_functions = [sum2, mean, median]
    for index, chosen_dict in enumerate(dict_list):
        print_details(population_list[index], chosen_dict, features_of_part_a, statistic_functions)

    print("\nQuestion 2:")


if __name__ == "__main__":
    main(sys.argv)
