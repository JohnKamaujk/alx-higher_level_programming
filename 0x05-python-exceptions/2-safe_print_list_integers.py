#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x integers of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Return:
        The number of elements printed.
    """

    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
