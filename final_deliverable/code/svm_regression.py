import numpy as np
import random
import statsmodels.api as sm
from statsmodels.tools import eval_measures
from util import train_test_split, load_file, calculate_r_squared
from sklearn import svm
import pandas as pd


def svm_regression(X_train, X_test, y_train, y_test):
    X_train = sm.add_constant(np.array(X_train))
    X_test = sm.add_constant(np.array(X_test))
    regr = svm.SVR(C=1, cache_size=7000)
    regr.fit(X_train, y_train)

    pred_train = regr.predict(X_train)
    pred_test = regr.predict(X_test)

    training_MSE = eval_measures.mse(y_train, pred_train)
    testing_MSE = eval_measures.mse(y_test, pred_test)
    r_squared = regr.score(X_test, y_test)
    print(training_MSE, testing_MSE, r_squared)

    df = pd.DataFrame(data={"expected": y_test, "predicted": pred_test})
    df.to_csv("../visualizations/svm_results.csv")
    return training_MSE, testing_MSE, r_squared


if __name__ == "__main__":
    X, y = load_file("./data/weekly_tracks.csv",
                     [
                         #  "Position",
                         #  "Artist",
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
                         #  "time_signature",
                     ],
                     )
    X = X.values.tolist()
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    training_MSE, testing_MSE, r_squared = svm_regression(
        X_train, X_test, y_train, y_test
    )
