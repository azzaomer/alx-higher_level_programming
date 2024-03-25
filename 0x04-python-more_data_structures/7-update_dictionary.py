#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in list(a_dictionary):
        if i == key:
            a_dictionary[i] = a_dictionary[key]
        else:
            a_dictionary[key] = value
    return a_dictionary


