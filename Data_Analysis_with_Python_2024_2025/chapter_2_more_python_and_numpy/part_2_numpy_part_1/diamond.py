#!/usr/bin/env python3

import numpy as np

def diamond(n):
    size = 2*n - 1
    e = np.eye(n, dtype=int)
    top = np.fliplr(e)[:-1]
    bot = e
    half = np.concatenate((top, bot))
    right = np.fliplr(half)[:, 1:]
    return np.concatenate((half, right), axis=1)

def main():
    pass

if __name__ == "__main__":
    main()
