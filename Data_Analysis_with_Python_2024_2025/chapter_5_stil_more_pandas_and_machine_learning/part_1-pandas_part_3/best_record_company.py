#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    publisher_woc_sum = df.groupby("Publisher")["WoC"].sum()
    best_publisher = publisher_woc_sum.idxmax()
    best_publisher_singles = df[df["Publisher"] == best_publisher]
    return best_publisher_singles

def main():
    best_company_df = best_record_company()
    print(best_company_df)
    

if __name__ == "__main__":
    main()
