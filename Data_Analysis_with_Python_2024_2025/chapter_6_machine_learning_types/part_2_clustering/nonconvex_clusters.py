#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy.stats
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = (labels == i)
        # Find the most common real label for points in cluster i
        new_label = scipy.stats.mode(real_labels[idx], keepdims=True)[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df =pd.read_csv("src/data.tsv", sep="\t")
    X = df[["X1", "X2"]]
    y = df["y"].values

    n_true_labels = len(np.unique(y))
    results = []

    for eps in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=eps)
        model.fit(X)
        labels = model.labels_

        n_outliers = np.sum(labels == -1)
        unique_clusters = set(labels) - {-1}
        n_clusters = len(unique_clusters)
        if n_clusters != n_true_labels:
            score = np.nan
        else:
            mask = (labels != -1)
            valid_labels = labels[mask]
            valid_y = y[mask]
            permutation = find_permutation(n_clusters, y, labels)
            perm_array = np.array(permutation)
            pred_y = perm_array[valid_labels]

            score = accuracy_score(valid_y, pred_y)

        results.append({
            "eps": eps,
            "Score": score,
            "Clusters": n_clusters,
            "Outliers": n_outliers
        })
    return pd.DataFrame(results).astype(float)

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
