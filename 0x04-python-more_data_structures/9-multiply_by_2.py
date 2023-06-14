#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b = a_dictionary.copy()

    for k, v in b.items():
        b[k] = v * 2

    return b
