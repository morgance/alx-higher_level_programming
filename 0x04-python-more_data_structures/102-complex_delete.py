#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for dicti in list_keys:
        if value == a_dictionary.get(dicti):
            del a_dictionary[dicti]

    return (a_dictionary)
