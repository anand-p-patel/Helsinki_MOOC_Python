#!/usr/bin/env python3
import pandas as pd


def read_series():  
    indices = []
    values = []
    
    while True:
        line = input("Enter index and value separated by space: ")
        
        if line.strip() == "":
            break
            
        parts = line.split() 
        
        if len(parts) != 2:
            raise ValueError("Every line must have exactly an index and value")
            
        indices.append(parts[0])
        values.append(parts[1])
        
    return pd.Series(values, index=indices, dtype=object)


def main():
    print("Please enter your Series elements (leave an empty line to finish):")
    try:
        series_data = read_series()
        print("\n--- Successfully Created Series ---")
        print(series_data)
        print(f"Data Type: {series_data.dtype}")
    except ValueError as err:
        print(f"\nExecution Stopped: {err}")
    pass

if __name__ == "__main__":
    main()
