#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for c in my_string:
        if c != 'c' and c != 'C':  # remove c
            new_str = new_str + c
    return new_str
