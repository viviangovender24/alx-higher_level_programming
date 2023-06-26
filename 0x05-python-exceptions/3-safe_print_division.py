#!/usr/bin/python3
def safe_print_division(a, b):  # divide
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(result))
    return res
