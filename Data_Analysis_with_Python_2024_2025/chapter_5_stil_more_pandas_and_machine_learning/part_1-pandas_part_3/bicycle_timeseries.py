#!/usr/bin/env python3

import pandas as pd


def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all").dropna(how="all",axis=1)
    parsed_date = df["Päivämäärä"].str.split(expand=True)

    months = {
        "tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, 
        "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, 
        "syys": 9, "loka": 10, "marras": 11, "joulu": 12
    }

    date_components = pd.DataFrame({
        "year": parsed_date[3].astype(int),
        "month": parsed_date[2].map(months),
        "day": parsed_date[1].astype(int),
        "hour": parsed_date[4].str.split(":").str[0].astype(int)
    })

    df.index = pd.to_datetime(date_components)

    df = df.drop(columns=["Päivämäärä"])

    return df


def main():
    df = bicycle_timeseries()
    print(df.head())
    print("\nIndex Type:", type(df.index))
    return None

if __name__ == "__main__":
    main()
