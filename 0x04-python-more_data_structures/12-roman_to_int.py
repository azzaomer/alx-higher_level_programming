#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# Initializing the result variable to zero
    result = 0
# Looping through the Roman Numeral string and adding the corresponding value to the result variable
    for i in range(len(roman_string)):
        if i > 0 and roman_dict[roman_string[i]] > roman_dict[roman_string[i-1]]:
            result += roman_dict[roman_string[i]] - 2 * roman_dict[roman_string[i-1]]
        else:
            result += roman_dict[roman_string[i]]
    return (result)
