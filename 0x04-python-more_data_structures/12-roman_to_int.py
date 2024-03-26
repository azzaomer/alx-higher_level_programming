#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to convert a Roman numeral to an integer
# ---------------------------------------------------

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for j in range(len(roman_string)):
        if j > 0 and roman_dic[roman_string[j]] > roman_dic[roman_string[j - 1]]:
            result += roman_dic[roman_string[j]] - 2 * roman_dic[roman_string[j - 1]]
        else:
            result += roman_dic[roman_string[j]]
    return result
