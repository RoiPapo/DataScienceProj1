import sys
from Data import *
from Statistics import sum2, median, mean, population_statistics


def main(argv):
    # default_path = 'cps09mar.csv'  # REMEMBER T0 CHANGE BEFORE HANDING
    # default_features = ['age', 'female', 'education', 'earnings', 'hours', 'week', 'marital']
    path = argv[1]
    features = argv[2]
    features_p1 = ['age', 'earnings', 'hours', 'week']
    print("Question 1:")
    data = load_data(path, features)
    all_dict = load_data(path, features)
    values = set([1])
    married_vals = set([1, 2, 3])
    female_dict, male_dict = filter_by_features(data, 'female', values)
    dict_list1 = [male_dict, female_dict, all_dict]
    pop_list = ["Men", "Women", "All"]
    statistic_functions = [sum2, mean, median]
    for index, chosen_dict in enumerate(dict_list1):
        print_details(pop_list[index], chosen_dict, features_p1, statistic_functions)

    print("\nQuestion 2:")
    stat_func_q2 = [mean, median]
    features_p2 = ['education', 'earnings', 'marital']
    pop_list2 = ["Married Women", "Unmarried Women"]
    married_dict, unmarried_dict = filter_by_features(female_dict, 'marital', married_vals)
    dict_list2 = [married_dict, unmarried_dict]
    print("If 0<=Y<=10, then:")
    for index, pop in enumerate(pop_list2):
        population_statistics(pop_list2[index], dict_list2[index], features_p2[0], features_p2[1], 0, 11, stat_func_q2)
    print(f"If 11<=Y<=20, then:")
    for index, pop in enumerate(pop_list2):
        population_statistics(pop_list2[index], dict_list2[index], features_p2[0], features_p2[1], 11, 21, stat_func_q2)


if __name__ == "__main__":
    main(sys.argv)
