#!/usr/bin/env python3

from math import sqrt

def solve_quadratic(a, b, c):
    root1 = (-b + sqrt((b**2)-4*a*c)) / (2*a)
    root2 = (-b - sqrt((b**2)-4*a*c)) / (2*a)
    return (root1, root2)


def main():
    a = float(input("Value of a:"))
    b = float(input("Value of b:"))
    c = float(input("Value of c:"))
    print(solve_quadratic(a,b,c))
    pass

if __name__ == "__main__":
    main()
