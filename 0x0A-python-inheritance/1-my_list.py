#!/usr/bin/python3
""" Contain MyList class"""


class MyList(list):
    """Class that extends the list base class"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
