import os
import pandas as pd


def municipalities_of_finland():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "municipal.tsv")

    df = pd.read_csv(file_path, sep="\t", index_col="Region 2018")
    return df["Akaa":"Äänekoski"]


def growing_municipalities(df):
    col_growth = "Population change from the previous year, %"

    return (df[col_growth] > 0).mean()


def main():
    df = municipalities_of_finland()

    proportion = growing_municipalities(df)

    print(f"Proportion of growing municipalities: {proportion * 100:.1f}%")


if __name__ == "__main__":
    main()