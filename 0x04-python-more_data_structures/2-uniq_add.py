#!/usr/bin/python3

def uniq_add(my_list=[]):
    set_list = set(my_list)
    sum_no = 0
    for no in set_list:
        sum_no += no
    return sum_no
