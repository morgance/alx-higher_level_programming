#!/usr/bin/python3

def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for x in list_num:
        if max_list > x:
            to_sub += x

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_an = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_an.keys())

    num = 0
    last_roma = 0
    list_num = [0]

    for i in roman_string:
        for r_num in list_keys:
            if r_num == i:
                if rom_an.get(i) <= last_roma:
                    num += to_subtract(list_num)
                    list_num = [rom_an.get(i)]
                else:
                    list_num.append(rom_an.get(i))

                last_roma = rom_an.get(i)

    num += to_subtract(list_num)

    return (num)
