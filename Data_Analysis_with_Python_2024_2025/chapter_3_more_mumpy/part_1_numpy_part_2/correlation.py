#!/usr/bin/env python3

from scipy.stats import pearsonr
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    sepal_len = data[:, 0]
    petal_len = data[:, 2]

    corr, _= pearsonr(sepal_len, petal_len)
    return corr

def correlations():
    data = load()
    return np.corrcoef(data, rowvar= False)

def main():
    np.fill_diagonal(c, 0)
    max_idx = np.unravel_index(np.argmax(c), c.shape)
    print(f"The most highly correlated pair is index {max_idx}")
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
