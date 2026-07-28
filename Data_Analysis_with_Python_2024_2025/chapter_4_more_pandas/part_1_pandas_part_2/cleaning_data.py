#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")

    def fix_name(name):
        if "," in name:
            last, first = name.split(",")
            name = f"{first.strip()} {last.strip()}"
        return name.title()
    
    df["President"] = df["President"].apply(fix_name)
    df["Vice-president"] = df["Vice-president"].apply(fix_name)

    df["Start"] = df["Start"].astype(str).str.split().str[0].astype(int)

    df["Last"] = pd.to_numeric(df["Last"], errors="coerce")
    df["Seasons"] = df["Seasons"].replace({"two":"2", "one":"1"}).astype(int)
    return df

def main():
    print(cleaning_data())
    return

if __name__ == "__main__":
    main()
