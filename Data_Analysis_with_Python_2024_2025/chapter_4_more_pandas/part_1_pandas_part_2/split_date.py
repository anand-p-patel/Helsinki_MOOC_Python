#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all").dropna(how="all",axis=1)
    
    split_df = df["Päivämäärä"].str.split(expand=True)
    split_df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    weekday_map = {
        "ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu",
        "pe": "Fri", "la": "Sat", "su": "Sun"
    }
    month_map = {
        "tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4,
        "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
        "syys": 9, "loka": 10, "marras": 11, "joulu": 12
    }

    split_df["Weekday"] = split_df["Weekday"].map(weekday_map)
    split_df["Month"] = split_df["Month"].map(month_map)

    split_df["Hour"] = split_df["Hour"].str.split(":").str[0]

    split_df = split_df.astype({
        "Day": int,
        "Month": int,
        "Year": int,
        "Hour": int
    })
    return split_df

def main():
    print(split_date())
    return
       
if __name__ == "__main__":
    main()
