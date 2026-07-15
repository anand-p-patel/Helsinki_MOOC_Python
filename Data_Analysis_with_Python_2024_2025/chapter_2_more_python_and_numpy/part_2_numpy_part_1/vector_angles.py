#!/usr/bin/env python3

import numpy as np
import scipy.linalg


def vector_angles(X, Y):
    len_x = np.sqrt(np.sum(np.square(X), axis = 1))
    len_y = np.sqrt(np.sum(np.square(Y), axis = 1))
    numerator = np.sum(np.multiply(X,Y), axis = 1)
    cos_angle = numerator / (len_x * len_y)
    return np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0)))

def main():
    X = np.array([[1, 0], 
                  [1, 1]])
    Y = np.array([[0, 1], 
                  [1, 1]])
    angles = vector_angles(X, Y)
    print("Calculated angles (in degrees):")
    print(angles)

if __name__ == "__main__":
    main()
