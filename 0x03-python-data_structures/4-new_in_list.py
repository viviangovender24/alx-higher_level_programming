#!/usr/bin/python3
def new_in_list(my_list, idx, element):  # Replace an element
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
        cpy = [x for x in my_list]
        cpy[idx] = element
        return (cpy)
