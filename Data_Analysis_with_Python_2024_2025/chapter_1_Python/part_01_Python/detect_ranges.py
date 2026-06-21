#!/usr/bin/env python3

#def detect_ranges(L):
#    ordered_list = sorted(L)
#    ranges = []
#    start_point = ordered_list[0]
#    for i in range(1, len(ordered_list)):
#        if ordered_list[i] == ordered_list[i-1] + 1 :
#            if start_point == ordered_list[i-1]:
#                ranges.append(start_point)
#            else:
#                ranges.append(ordered_list[i-1]+1)
#            start_point = ordered_list[i]
#    if start_point == ordered_list[-1]:
#        ranges.append(start_point)
#    else:
#        ranges.append(ordered_list[-1] + 1)
#        
#    return ranges


def detect_ranges(L):
    ordered_list = sorted(L)
    ranges = []
    start = ordered_list[0]

    for i in range(1, len(ordered_list)):
        if ordered_list[i] != ordered_list[i-1] + 1:  # sequence broke
            end = ordered_list[i-1]
            if start == end:          # single number
                ranges.append(start)
            else:                     # it's a range
                ranges.append((start, end + 1))
            start = ordered_list[i]  # start new range

    # handle the last range after loop ends
    end = ordered_list[-1]
    if start == end:
        ranges.append(start)
    else:
        ranges.append((start, end + 1))

    return ranges

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
