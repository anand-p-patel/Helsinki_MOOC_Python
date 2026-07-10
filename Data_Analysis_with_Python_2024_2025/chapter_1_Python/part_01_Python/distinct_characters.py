#!/usr/bin/env python3

def distinct_characters(L):
    results = {}
    for i in L:
        results[i] = len(set(i))
    return results

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
