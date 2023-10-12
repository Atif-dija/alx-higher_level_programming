#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    num = 0
    T = 0
    dgts = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for s in reversed(roman_string):
        num = dgts[s]
        if T < num * 5:
            T += num
        else:
            T -= num
    return T
