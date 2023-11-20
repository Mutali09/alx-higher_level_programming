#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for p in range(x):
            if type(my_list[p]) is int:
                print("{:d}".format(my_list[p]), end="")
                count += 1
                print()
        return (count)
    except IndexError:
        print()
        return (count)
