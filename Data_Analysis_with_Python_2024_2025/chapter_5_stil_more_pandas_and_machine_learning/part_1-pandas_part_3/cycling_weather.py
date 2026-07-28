#!/usr/bin/env python3

import pandas as pd

def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all", axis=0).dropna(how="all", axis=1)
    
    date_df = df["Päivämäärä"].str.split(expand=True)
    date_df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    
    weekday_map = {
        "ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu",
        "pe": "Fri", "la": "Sat", "su": "Sun"
    }
    month_map = {
        "tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4,
        "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
        "syys": 9, "loka": 10, "marras": 11, "joulu": 12
    }
    
    date_df["Weekday"] = date_df["Weekday"].map(weekday_map)
    date_df["Day"] = date_df["Day"].astype(int)
    date_df["Month"] = date_df["Month"].map(month_map).astype(int)
    date_df["Year"] = date_df["Year"].astype(int)
    date_df["Hour"] = date_df["Hour"].str.split(":").str[0].astype(int)
    
    measurements = df.drop(columns=["Päivämäärä"])
    return pd.concat([date_df, measurements], axis=1)

def cycling_weather():
    cycling = split_date_continues()
    weather = pd.read_csv("src/kumpula-weather-2017.csv")

    merged = pd.merge(
        cycling,
        weather,
        left_on=["Year", "Month", "Day"],
        right_on=["Year", "m", "d"]
    )
    result = merged.drop(columns=["m", "d", "Time", "Time zone"])
    return result

def main():
    print(cycling_weather())
    return

if __name__ == "__main__":
    main()
