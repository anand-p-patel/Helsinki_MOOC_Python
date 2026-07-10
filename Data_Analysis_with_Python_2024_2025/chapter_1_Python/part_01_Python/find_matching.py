#!/usr/bin/env python3

def find_matching(L, pattern):
    matches = []
    for i, x in enumerate(L):
        if pattern in x:
            matches.append(i)

    return matches

def main():
    pass

if __name__ == "__main__":
    main()
