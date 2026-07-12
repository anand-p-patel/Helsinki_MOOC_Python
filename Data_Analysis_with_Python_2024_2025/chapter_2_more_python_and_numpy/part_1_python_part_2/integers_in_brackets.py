#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    ints_only = re.findall(r"\[\s*[+-]?\d+\s*\]", s)
    stripped_ints = []
    for i in ints_only:
        stripped_ints.append(int(i.strip("[] ")))
    return stripped_ints

def main():
    pass

if __name__ == "__main__":
    main()
