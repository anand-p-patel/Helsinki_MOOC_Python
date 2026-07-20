#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    s1 = pd.Series(L1, index = ["a", "b", "c"])
    s2 = pd.Series(L2, index = ["a", "b", "c"])
    return (s1, s2)
    
def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del s2["b"]
    return (s1, s2)
    
def main():
    data1 = [10, 20, 30]
    data2 = [100, 200, 300]

    s1, s2 = create_series(data1, data2)
    
    s1_mod, s2_mod = modify_series(s1, s2)

    print("Modified s1: ")
    print(s1_mod)
    print("\n Modified s2: ")
    print(s2_mod)

    print("\n s1  + s2 : ")
    result = s1_mod + s2_mod
    print(result)

    
if __name__ == "__main__":
    main()
