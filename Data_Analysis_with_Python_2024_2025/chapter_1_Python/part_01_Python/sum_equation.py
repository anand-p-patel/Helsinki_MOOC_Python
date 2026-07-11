#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"
    return " + ".join(map(str, L)) + " = " + str(sum(L))

def main():
    pass

if __name__ == "__main__":
    main()
