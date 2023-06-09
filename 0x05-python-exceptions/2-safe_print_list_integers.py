#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):  # 1st x
    co = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            co += 1
        except (ValueError, TypeError):
            continue
    print()
    return co
