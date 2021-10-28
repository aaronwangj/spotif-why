import random
import pandas as pd
import math
import numpy as np


def load_file(file_path, x_var):
    """
    input:
        file_path: the path to the data file
        x_var:
            - for simple linear regression: the name of the independent variable
            - for multiple linear regression: a list of the names of the independent
            variables
            NOTE: to access a column in a pandas dataframe (df), you do
                    df['column_name'].values;
                to access multiple columns, you need df[['column_name1',
                    'column_name2', ..., ]]

    output:
        X: python list of independent variables values
        y: python list of the dependent variable
            values (i.e. 'cnt')
    """
    df = pd.read_csv(file_path)
    df.drop_duplicates(subset=['id'], inplace=True)
    df = df.sort_values('popularity', ascending=False).drop_duplicates(
        subset=['Track Name', 'Artist']).sort_index()

    print(df.shape)
    # one_hot = pd.get_dummies(df['Artist'])
    # X = pd.concat([df[x_var], one_hot], axis=1)

    X = df[x_var]
    y = df["popularity"].values / 100
    return X, y


def split_data_randomly(data, prob):
    """
    input:
    - data: a list of pairs of x,y values
    - prob: the fraction of the dataset that will be testing data, typically
    prob=0.2

    output:
    - a tuple of two lists with training data pairs and testing data pairs,
    respectively.
    """
    # placeholders - do not change this. first list: training data,
    # second list: testing data
    results = [], []
    # TODO: Split data randomly into fractions [prob, 1 - prob]. populate the lists
    # in the tuple
    random.shuffle(data)
    train_len = int(len(data) * (1 - prob))
    results[0].extend(data[:train_len])
    results[1].extend(data[train_len:])
    # return - you should not change this
    return results


def train_test_split(x, y, test_pct=0.2):
    """
    input:
        x: list of x values
        y: list of independent values
        test_pct: percentage of the data that is testing data (0.2 by default).

    output: x_train, x_test, y_train, y_test lists
    """
    # placeholders
    x_train, x_test, y_train, y_test = [], [], [], []
    # TODO: Split the features X and the labels y into x_train, x_test and
    # y_train, y_test as specified by test_pct. You may want to use split_data_randomly
    # in this function
    train, test = split_data_randomly(list(zip(x, y)), test_pct)
    x_train.extend([pair[0] for pair in train])
    x_test.extend([pair[0] for pair in test])
    y_train.extend([pair[1] for pair in train])
    y_test.extend([pair[1] for pair in test])
    return x_train, x_test, y_train, y_test


def calculate_r_squared(y_test, y_predicted):
    """
    Calculate the r-squared value

    Note: use the funciont R-Squared = 1 - SSE/SSTO

    input:
        y_test (list): the actual y values
        y_predicted (list): the predicted y values from the model

    output:
        r-squared (float)
    """
    sample_mean = sum(y_test) / len(y_test)
    SSE = 0
    for i in range(len(y_test)):
        SSE += (y_test[i] - y_predicted[i]) ** 2
    SSTO = sum([(y - sample_mean) ** 2 for y in y_test])

    return 1 - SSE / SSTO
