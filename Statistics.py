def sum_of_values(values):
    """
    :param values: list of values
    :return: sum of values
    """
    total = 0
    for value in values:
        total += value
    return total


def mean(values):
    """
    :param values:
    :return: mean of values
    """
    return sum(values) / len(values)


def median(values):
    """
    :param values:
    :return: median of values
    """
    values.sort()
    if len(values) % 2 != 0:
        return values[(len(values) - 1) / 2]
    return (values[len(values) // 2] + values[(len(values) // 2) - 1]) / 2


def population_statistics(population, data, feature_1, feature_2, min_val, max_val, statistics_functions):
    """
    :param statistics_functions: list of statisic methods
    :param max_val: the maximum value of feature_1
    :param min_val: the minimum value of feature_1
    :param feature_2: a feature's name from the data set
    :param feature_1: a feature's name from the data set
    :param data: dictionary
    :param population: population name string
    :return: collecting the records for which min_val<=feature_1<=max_val, and displaying statistic charts on a
    specific population's data's feature_2
    """
    for i in range(data[feature_1]):
        if min_val <= data[feature_1][i] <= max_val:
            filter_by_features(data, feature_1, values)
    for population in population_type:
        for method in statistics_functions:
            print_details(population, dict_of_fitting_values, features, method)
