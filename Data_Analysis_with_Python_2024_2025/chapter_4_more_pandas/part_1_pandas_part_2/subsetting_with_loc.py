import os
import pandas as pd


def subsetting_with_loc():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "municipal.tsv")

    df = pd.read_csv(file_path, sep="\t", index_col="Region 2018")

    cols = [
        "Population",
        "Share of Swedish-speakers of the population, %",
        "Share of foreign citizens of the population, %",
    ]

    return df.loc["Akaa":"Äänekoski", cols]


def main():
    print(subsetting_with_loc())


if __name__ == "__main__":
    main()