#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_letters = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    n = 0
    las = 0

    for letter in roman_string:
        for eleme in roman_letters:
            if letter == eleme[0]:
                if las == 0 or las >= eleme[1]:
                    n += eleme[1]
                elif las < eleme[1]:
                    n += eleme[1] - (las * 2)

                las = eleme[1]

    return n
