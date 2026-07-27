import os
import pandas as pd


def snow_depth():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "kumpula-weather-2017.csv")
    df = pd.read_csv(file_path)
    return df["Snow depth (cm)"].max()


def main():
    max_snow = snow_depth()
    print(f"Max snow depth: {max_snow:.1f}")


if __name__ == "__main__":
    main()