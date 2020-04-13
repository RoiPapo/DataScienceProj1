def sum_of_values(values):
    """

    :param values:
    :return:
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
    pass
