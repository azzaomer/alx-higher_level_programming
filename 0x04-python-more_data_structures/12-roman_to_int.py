#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to convert a Roman numeral to an integer
# ---------------------------------------------------

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for j in range(len(roman_string)):
        if j > 0 and dic[roman_string[j]] > dic[roman_string[j - 1]]:
            result += dic[roman_string[j]] - 2 * dic[roman_string[j - 1]]
        else:
            res += dic[roman_string[j]]
    return res
