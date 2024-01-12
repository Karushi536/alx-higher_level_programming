#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.
    """
    # Check if the key exists before deleting
    if key in a_dictionary:
        del a_dictionary[key]
    
    return a_dictionary
