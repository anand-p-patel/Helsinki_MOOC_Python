#!/usr/bin/env python3

def transform(s1, s2):
    s1_new = list(map(int, s1.split()))
    s2_new = list(map(int, s2.split()))
    new_list = [x*y for x,y in zip(s1_new,s2_new)]
    return new_list

def main():
    pass

if __name__ == "__main__":
    main()
