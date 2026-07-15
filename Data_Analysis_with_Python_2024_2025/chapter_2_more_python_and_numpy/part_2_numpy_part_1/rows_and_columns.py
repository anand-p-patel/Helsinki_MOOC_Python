#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    rows = []
    array_a = np.array(a)
    for row in array_a:
        rows.append(row)

    return rows

def get_columns(a):
    columns = []
    array_a = np.array(a)
    for col in array_a.T:
        columns.append(col)
    return columns

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
