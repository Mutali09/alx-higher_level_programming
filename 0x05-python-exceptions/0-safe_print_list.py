#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for p in range(x):
            print(my_list[p], end ="")
            count += 1
    except IndexError:
        pass
    print ()
    return (count)
