#!/usr/bin/env python3

import sys
import numpy as np

def summary(filename):
    numbers = []
    with open(filename) as file:
        for line in file:
            try:
                nums = float(line.strip())
                numbers.append(nums)
            except ValueError:
                pass
    sum_nums = np.sum(numbers)
    mean_nums = np.mean(numbers)
    std_dev_nums = np.std(numbers, ddof=1)

    return (sum_nums, mean_nums, std_dev_nums)

def main():
    for filename in sys.argv[1:]:
        s, a, d = summary(filename)
        print(f"File: {filename} Sum: {s:.6f} Average: {a:.6f} Stddev: {d:.6f}")
    pass

if __name__ == "__main__":
    main()
