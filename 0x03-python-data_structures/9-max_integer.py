#!/usr/bin/python3
def max_integer(my_list=[]):  # max int
    if not my_list:
        return None

    mx = min(my_list)
    for i in my_list:
        if i > mx:
            mx = i
    return mx
