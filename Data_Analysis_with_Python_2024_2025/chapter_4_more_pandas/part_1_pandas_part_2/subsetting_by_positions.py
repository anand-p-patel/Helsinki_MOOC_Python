import os
import pandas as pd


def subsetting_by_positions():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "UK-top40-1964-1-2.tsv")


    df = pd.read_csv(file_path, sep="\t")

    cols = [df.columns.get_loc("Title"), df.columns.get_loc("Artist")]

    return df.iloc[:10, cols]


def main():
    print(subsetting_by_positions())


if __name__ == "__main__":
    main()
