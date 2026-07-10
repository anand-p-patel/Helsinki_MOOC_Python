#!/usr/bin/env python3

def reverse_dictionary(d):
    inverted = {}
    for key, values in d.items():
        for finnish_word in values:
            if finnish_word in inverted:
                inverted[finnish_word].append(key)
            else:
                inverted[finnish_word] = [key]
    return inverted

def main():
    pass

if __name__ == "__main__":
    main()
