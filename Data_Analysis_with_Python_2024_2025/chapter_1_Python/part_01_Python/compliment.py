#!/usr/bin/env python3

#make a function that takes a string and returns the compliment of the string


def main():
    string = input("What country are you from? ")
    compliment = get_compliment(string)
    print(f"I have heard that {string} {compliment}")


def get_compliment(string):
    return f"is a beautiful country."


if __name__ == "__main__":
    main()
