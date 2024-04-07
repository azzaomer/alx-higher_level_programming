#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elem_counter = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            elem_counter += 1
    except IndexError:
        pass
    finally:
        print()
        return elem_counter
