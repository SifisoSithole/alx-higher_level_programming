#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(test_string, str):
        return 0
    se = {
            "R": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    res = 0
    roman_string += 'R'
    i = 0
    while i < len(roman_string) - 1:
        if se[roman_string[i]] < se[roman_string[i+1]]:
            res += se[roman_string[i+1]] - se[roman_string[i]]
            i += 2
        else:
            res += se[roman_string[i]]
            i += 1
    return res
