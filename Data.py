import pandas as pd


def load_data(path, features):
    features = ['age', 'earnings', 'hours', 'week', 'female']
    path = 'hw1_sample_input.csv'
    data3 = pd.read_csv('cps09mar.csv')
    data2 = pd.read_csv(path)
    df = pd.DataFrame(data2, columns=features)
    print(df)


def filter_by_features(data, feature, vlaues):
    pass
