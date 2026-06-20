#!/usr/bin/env python3

def main():
    num_a = 0
    num_b = 0
    for num_a in range(1,7):
        for num_b in range(1,7):
            if num_a + num_b == 5:
                print(f"({num_a},{num_b})")
    pass

if __name__ == "__main__":
    main()
