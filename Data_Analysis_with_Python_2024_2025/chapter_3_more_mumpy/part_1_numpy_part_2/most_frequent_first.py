#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    values, counts = np.unique(a[:, c], return_counts = True)
    frequency_scores = counts[np.searchsorted(values, a[:, c])]
    order = np.argsort(frequency_scores)
    return a[order[::-1]]

def main():
    pass

if __name__ == "__main__":
    main()
