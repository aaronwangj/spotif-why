import numpy as np
import random
import statsmodels.api as sm
import pandas as pd
from statsmodels.tools import eval_measures
from util import train_test_split, load_file, calculate_r_squared
from sklearn import svm


def multiple_regression(X_train, X_test, y_train, y_test):
    """
    A multiple linear regression using StatsModel
    Inputs:
    - X_train, X_test, y_train, y_test: lists of training and testing values

    Outputs:
    - The Mean Squared Error value when applying the model on the training
    dataset (training_MSE)
    - The Mean Squared Error value when applying the model on the testing
    dataset (testing_MSE)
    - The R-Squared value when applying the model on the *training* dataset
    (training_R2)
    """
    # TODO: Use StatsModels to create the Linear Model and Output R-squared
    X_train = sm.add_constant(np.array(X_train))
    print(X_train.shape)
    X_test = sm.add_constant(np.array(X_test))
    model = sm.OLS(np.array(y_train), X_train)
    results = model.fit()
    # TODO: Prints out the Report
    print(results.summary())
    # TODO: print R-squared, test MSE & train MSE
    pred_train = results.predict(X_train)
    pred_test = results.predict(X_test)
    print(np.mean(pred_train))

    training_MSE = eval_measures.mse(y_train, pred_train)
    testing_MSE = eval_measures.mse(y_test, pred_test)
    testing_R2 = calculate_r_squared(y_test, pred_test)
    print(training_MSE, testing_MSE, testing_R2)

    df = pd.DataFrame(data={"expected": y_test, "predicted": pred_test})
    df.to_csv("../visualizations/regression/regression_results.csv")
    return training_MSE, testing_MSE, testing_R2


if __name__ == "__main__":
    # TODO: Call load_file; x_var should be a list
    X, y = load_file(
        "./data/clean.csv",
        [
            # "Position",
            # "Streams",
            "danceability",
            "energy",
            # "key",
            "loudness",
            "mode",
            "speechiness",
            "acousticness",
            "instrumentalness",
            "liveness",
            "valence",
            # "tempo",
            # "duration_ms",
            # "time_signature",
        ],
    )
    X = X.values.tolist()
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    training_MSE, testing_MSE, testing_R2 = multiple_regression(
        X_train, X_test, y_train, y_test
    )
