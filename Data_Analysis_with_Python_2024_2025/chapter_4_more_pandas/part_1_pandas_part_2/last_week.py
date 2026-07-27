#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t",
                     na_values=["New", "Re"])
    sub = df[df['LW'].notnull()].copy()

    peak_pos = sub['Peak Pos'].where(
        (sub['Peak Pos'] < sub['Pos']) | (sub['Peak Pos'] == sub['LW'])
    )


    sub['Pos'] = sub['LW'].astype(int)
    sub['WoC'] = sub['WoC'] - 1
    sub['LW'] = np.nan
    sub['Peak Pos'] = peak_pos

    res = sub.set_index('Pos').reindex(range(1, len(df) +1 )).reset_index()
    res = res[df.columns]

    return res

    
def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
