#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t")

    rows, cols = df.shape

    print(f"Shape: {rows},{cols}")
    print("Columns:")
    for col in df.columns:
        print(col)


if __name__ == "__main__":
    main()
