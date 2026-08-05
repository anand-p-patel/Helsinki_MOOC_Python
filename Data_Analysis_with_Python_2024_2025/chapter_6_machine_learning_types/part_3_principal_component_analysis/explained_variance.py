#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def explained_variance():
    df = pd.read_csv("src/data.tsv", sep="\t")
    variances = df.var().values
    pca = PCA()
    pca.fit(df)
    return variances, pca.explained_variance_

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    v_str = " ".join([f"{x:.3f}" for x in v])
    ev_str = " ".join([f"{x:.3f}" for x in ev])
    
    print(f"The variances are: {v_str}")
    print(f"The explained variances after PCA are: {ev_str}")
    
    # Plot the cumulative explained variances
    plt.plot(np.arange(1, len(ev) + 1), np.cumsum(ev), marker='o')
    plt.title("Cumulative Explained Variance")
    plt.xlabel("Number of terms in the cumulative sum")
    plt.ylabel("Cumulative sum")
    plt.show()
if __name__ == "__main__":
    main()
