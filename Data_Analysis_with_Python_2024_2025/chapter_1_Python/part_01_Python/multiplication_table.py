#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()  # moves to next line after each row
    pass

if __name__ == "__main__":
    main()
