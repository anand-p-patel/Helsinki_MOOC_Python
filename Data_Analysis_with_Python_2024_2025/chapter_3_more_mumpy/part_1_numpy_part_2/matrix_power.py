#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    if n < 0:
        a = np.linalg.inv(a)
        n = -n
    return reduce(lambda x, y: x @ y, (a for _ in range(n)))

def main():
    return

if __name__ == "__main__":
    main()
