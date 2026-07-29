#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")

    X = df.iloc[:, 0:5]
    y = df.iloc[:, 5]

    scores = []

    model = LinearRegression(fit_intercept=True)
    model.fit(X,y)
    scores.append(model.score(X,y))

    for col in X.columns:
        X_single = X[[col]]

        model_single = LinearRegression(fit_intercept=True)
        model_single.fit(X_single, y)
        scores.append(model_single.score(X_single, y))
    return scores
    
def main():
    scores = coefficient_of_determination()

    print(f"R2-score with feature(s) X: {scores[0]}")
    for i in range(1, len(scores)):
        print(f"R2-score with feature(s) X{i}: {scores[i]}")
if __name__ == "__main__":
    main()
