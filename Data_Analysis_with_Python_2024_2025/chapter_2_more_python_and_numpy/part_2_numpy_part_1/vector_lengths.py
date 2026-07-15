#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(np.square(a), axis = 1))

def main():
    test_array = np.array([[3, 4],
                           [6, 8],
                           [0, 5]])
    lengths = vector_lengths(test_array)

    print("Input array:")
    print(test_array)
    print("\nCalculated lengths:")
    print(lengths)
if __name__ == "__main__":
    main()
