#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = []
    for a, b in a_dictionary.items():
        if b == value:
            key.append(a)

    for a in key:
        del a_dictionary[a]

    return a_dictionary
