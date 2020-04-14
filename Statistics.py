def sum_of_values(values):
    """

    :param values: list of values
    :return: sum of values
    """
    return sum(values)


def mean(values):
    """

    :param values:
    :return:
    """
    return sum(values) / len(values)


def median(values):
    """

    :param values:
    :return:
    """
    values.sort()
    if len(values) % 2 != 0:
        return values[(len(values) - 1) / 2]
    else:
        return (values[len(values) // 2] + values[(len(values) // 2) - 1]) / 2


def population_statistics(population, data, feature_1, feature_2, min__val, max_val, statistics_functions):
    """
        :param statistics_functions:
        :param max_val:
        :param min__val:
        :param feature_2:
        :param feature_1:
        :param data:
        :param population
        :param values:
        :return:
        """
    pass
