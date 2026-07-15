#!/usr/bin/env python3

def extract_numbers(s):
    numbers = []
    for word in s.split():
        try:
            numbers.append(int(word))
        except ValueError:
            try:
                numbers.append(float(word))
            except ValueError:
                pass
                    
    return numbers

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
