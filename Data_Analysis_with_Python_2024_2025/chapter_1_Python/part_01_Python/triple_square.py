#!/usr/bin/env python3

def triple(x):
    return x*3

def square(x):
    return x**2



def main():
    for x in range(1,11):
        trip = triple(x)
        squ = square(x)
        if squ > trip:
            break
        print(f"triple({x})=={trip} square({x})=={squ}")

if __name__ == "__main__":
    main()
