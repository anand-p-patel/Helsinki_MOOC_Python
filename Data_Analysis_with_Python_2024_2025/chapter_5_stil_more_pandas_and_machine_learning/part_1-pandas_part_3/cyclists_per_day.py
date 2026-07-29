#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def cyclists_per_day():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all").dropna(how="all", axis=1)

    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "hour"]

    months = {
        "tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, 
        "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, 
        "syys": 9, "loka": 10, "marras": 11, "joulu": 12
    }

    d["Month"] = d["Month"].map(months)

    d["Year"] = d["Year"].astype(int)
    d["Day"] = d["Day"].astype(int)

    df_measurements = df.drop(columns=["Päivämäärä"])
    df_combined = pd.concat([d[["Year","Month","Day"]], df_measurements], axis=1)
    daily_counts = df_combined.groupby(["Year", "Month", "Day"]).sum()
    return daily_counts
    
def main():
    df = cyclists_per_day()
    august_2017 = df.loc[(2017, 8)]
    august_2017.plot()

    plt.title("Cyclists per day in Helsinki - August 2017")
    plt.xlabel("Day of Month")
    plt.ylabel("Number of Cyclists")
    
    plt.show()

if __name__ == "__main__":
    main()
