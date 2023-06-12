#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    le = len(my_list)   # replace
    if 0 <= idx < le:
        my_list[idx] = element
    return (my_list)
