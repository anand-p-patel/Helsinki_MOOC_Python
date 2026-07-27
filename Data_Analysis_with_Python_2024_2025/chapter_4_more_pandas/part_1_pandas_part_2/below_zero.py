#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return (df["Air temperature (degC)"] < 0).sum()

def main():
    days = below_zero()
    print(f"Number of days below zero: {days}")
    
if __name__ == "__main__":
    main()
