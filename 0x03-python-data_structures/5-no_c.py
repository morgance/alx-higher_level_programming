#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for alpha in my_string:
        if alpha != 'c' and alpha != 'C':
            new_string += alpha
    return (new_string)
