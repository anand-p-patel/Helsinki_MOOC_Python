#!/usr/bin/env python3

import scipy
import scipy.stats
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        mode_res = scipy.stats.mode(real_labels[idx], keepdims=True)
        new_label = mode_res[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    iris = load_iris()
    X, y = iris.data, iris.target

   
    model = KMeans(n_clusters=3, random_state=0, n_init=10)
    model.fit(X)

    permutation = find_permutation(3, y, model.labels_)

    perm_array = np.array(permutation).ravel()
    new_labels = perm_array[model.labels_]
    return accuracy_score(y, new_labels)

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()