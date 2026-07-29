#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)

    X = x[:, np.newaxis]

    model.fit(X, y)

    return model.coef_[0], model.intercept_
    
def main():
    x = np.array([1,2,3])
    y = np.array([2,3.5,4])

    slope, intercept = fit_line(x, y)

    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")

    plt.scatter(x, y, color= 'blue', label= 'Data points')
    y_fit = slope * x + intercept

    plt.plot(x, y_fit, color= 'red', label='Fitted line')

    plt.title("Linear Regression Fit")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    plt.show()
if __name__ == "__main__":
    main()
