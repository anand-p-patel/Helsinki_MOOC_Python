#!/usr/bin/env python3
import pandas as pd
from sklearn.linear_model import LinearRegression


def split_date(df):
    split_df = df["Päivämäärä"].str.split(expand=True)
    split_df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    month_map = {
        "tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4,
        "touko": 5, "kesä": 6, "heinä": 7, "elo": 8,
        "syys": 9, "loka": 10, "marras": 11, "joulu": 12
    }
    split_df["Month"] = split_df["Month"].map(month_map)
    split_df["Hour"] = split_df["Hour"].str.split(":").str[0]

    return split_df.astype({"Day": int, "Month": int, "Year": int, "Hour": int})


def cycling_weather_continues(station):
    weather = pd.read_csv("src/kumpula-weather-2017.csv")
    cycling = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    cycling.columns = cycling.columns.str.strip()
    weather.columns = weather.columns.str.strip()

    cycling = cycling.dropna(how="all", axis=0).dropna(how="all", axis=1)

    # The raw data has a single Finnish date column; split it into Year/Month/Day.
    date_df = split_date(cycling)
    cycling = pd.concat([date_df, cycling.drop(columns=["Päivämäärä"])], axis=1)

    # Sum the station's hourly counts into daily counts.
    station_sums = cycling.groupby(["Year", "Month", "Day"])[station].sum().reset_index()

    # The weather data uses lowercase 'm' and 'd' for month and day.
    merged = pd.merge(station_sums, weather,
                      left_on=["Year", "Month", "Day"],
                      right_on=["Year", "m", "d"])

    # A few days are missing the snow depth measurement.
    merged = merged.ffill()

    features = ["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]
    X = merged[features]
    y = merged[station]

    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)
    return model.coef_, model.score(X, y)

def main():
    station = "Baana"
    coefficients, score = cycling_weather_continues(station)

    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coefficients[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coefficients[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coefficients[2]:.1f}")
    print(f"Score: {score:.2f}")

if __name__ == "__main__":
    main()
