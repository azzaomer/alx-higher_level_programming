#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    k = 2
    new_dict = {}
    for i in a_dictionary:
        new_dict[i] = a_dictionary[i] * k
    return (new_dict)
