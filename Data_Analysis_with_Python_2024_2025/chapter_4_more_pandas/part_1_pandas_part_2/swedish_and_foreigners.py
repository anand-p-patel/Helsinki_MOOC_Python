#!/usr/bin/env python3

import pandas as pd

import os
import pandas as pd

def swedish_and_foreigners():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "municipal.tsv")
    
    df = pd.read_csv(file_path, sep="\t", index_col="Region 2018")

    df = df.loc["Akaa":"Äänekoski"]

    col_swedish = "Share of Swedish-speakers of the population, %"
    col_foreign = "Share of foreign citizens of the population, %"
    col_pop = "Population"

    mask = (df[col_swedish] > 5.0) & (df[col_foreign] > 5.0)
    subset = df[mask]

    return subset[[col_pop, col_swedish, col_foreign]]

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
