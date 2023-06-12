#!/usr/bin/python3

def max_integer(my_list=[]):
    leng = len(my_list)

    if leng == 0:
        return (None)

    int_max = my_list[0]

    for i in range(1, leng):
        if my_list[i] > int_max:
            int_max = my_list[i]
    return (int_max)
