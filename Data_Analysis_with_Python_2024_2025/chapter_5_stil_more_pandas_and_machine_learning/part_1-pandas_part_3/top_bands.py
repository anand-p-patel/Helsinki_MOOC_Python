#!/usr/bin/env python3

import pandas as pd

def top_bands():
    top40 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    bands = pd.read_csv("src/bands.tsv", sep="\t")

    top40["Artist"]= top40["Artist"].str.upper()
    bands["Band"] = bands["Band"].str.upper()
    merged = pd.merge(
        top40,
        bands,
        left_on="Artist",
        right_on="Band"
    )
    return merged

def main():
    merged_df = top_bands()
    print(merged_df.head())
    return

if __name__ == "__main__":
    main()
