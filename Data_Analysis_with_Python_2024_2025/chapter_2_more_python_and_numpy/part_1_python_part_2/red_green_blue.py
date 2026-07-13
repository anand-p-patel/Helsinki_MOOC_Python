#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename) as file:
        next(file)
        for line in file:
            line = line.strip()
            parts = re.findall(r"\S+", line)
            line = "\t".join([parts[0], parts[1], parts[2], " ".join(parts[3:])])
            result.append(line)
    return result


def main():
    pass

if __name__ == "__main__":
    main()
