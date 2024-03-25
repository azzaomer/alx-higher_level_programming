#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        k = 2
        new_dict = {}
        new_dict[i] = a_dictionary[i] * k
    return (new_dict)
