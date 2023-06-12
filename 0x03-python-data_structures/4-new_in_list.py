#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_count = len(my_list)

    rep_list = my_list[:]

    if 0 <= idx < list_count:
        rep_list[idx] = element
    return (rep_list)
