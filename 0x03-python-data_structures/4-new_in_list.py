#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my = my_list.copy()
    if idx < 0:
        return my
    elif idx >= len(my_list):
        return my
    else:
        my[idx] = element
        return my
