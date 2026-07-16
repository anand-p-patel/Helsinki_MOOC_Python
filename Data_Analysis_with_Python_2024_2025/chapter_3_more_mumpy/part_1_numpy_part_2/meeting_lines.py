#!/usr/bin/python3
import sys
import numpy as np

np.linalg.linalg = np.linalg
sys.modules['numpy.linalg.linalg'] = np.linalg

def meeting_lines(a1, b1, a2, b2):
    A = np.array([
        [-a1, 1],
        [-a2, 1]
    ])
    b = np.array([b1, b2])
    result = np.linalg.solve(A,b)
    return result[0], result[1]

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
