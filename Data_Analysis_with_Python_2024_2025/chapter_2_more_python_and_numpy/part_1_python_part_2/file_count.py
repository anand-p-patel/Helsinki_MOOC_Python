#!/usr/bin/env python3

import sys

def file_count(filename):
    file_count_num = 0
    word_count = 0
    char_count = 0
    with open(filename) as file:
        for line in file:
            file_count_num += 1
            char_count += len(line)
            for word in line.split():
                word_count += 1
    return (file_count_num, word_count, char_count)

def main():
    for filename in sys.argv[1:]:
        l, w, c = file_count(filename)
        print(f"{l}\t{w}\t{c}\t{filename}")


if __name__ == "__main__":
    main()
