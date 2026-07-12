#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    with open(filename, "r") as file:
        lines = []
        for line in file:
           match = re.search("\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+(\S+)", line)
           if match:
            match_tuple = (int(match.group(1)), match.group(2), int(match.group(3)), int(match.group(4)), int(match.group(5)), match.group(6))
            lines.append(match_tuple)
    return lines

def main():
    pass

if __name__ == "__main__":
    main()
