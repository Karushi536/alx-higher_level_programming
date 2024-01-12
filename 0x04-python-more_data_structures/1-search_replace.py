#!/usr/bin/python3

def search_replace(my_list, search, replace):
    clist = my_list.copy()
    for i in range(len(clist)):
        if clist[i] == search:
            clist[i] = replace
    return clist
