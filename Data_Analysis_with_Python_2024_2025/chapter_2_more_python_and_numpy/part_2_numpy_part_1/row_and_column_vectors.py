#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    rows = []
    array_a = np.array(a)
    for row in array_a:
        rows.append(row.reshape(1, -1))

    return rows


def get_column_vectors(a):
    columns = []
    array_a = np.array(a)
    for col in array_a.T:
        columns.append(col.reshape(-1, 1))
    return columns

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
