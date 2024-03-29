#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set."""
    diff_1 = set_1.difference(set_2)
    diff_2 = set_2.difference(set_1)
    result_set = diff_1.union(diff_2)
    return result_set
