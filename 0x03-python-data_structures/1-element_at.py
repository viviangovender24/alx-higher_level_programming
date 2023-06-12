#!/usr/bin/python3
def element_at(my_list, idx):
    le = len(my_list)
    return (my_list[idx] if 0 <= idx < le else None)
