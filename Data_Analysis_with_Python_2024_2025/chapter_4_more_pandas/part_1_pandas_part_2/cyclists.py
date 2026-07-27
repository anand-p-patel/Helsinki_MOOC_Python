#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all")
    df = df.dropna(how="all",axis=1)
    return df


def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()
