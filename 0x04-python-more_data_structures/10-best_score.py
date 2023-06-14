#!/usr/bin/python3

def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if a_dictionary:
        max_key = ""
        max_value = 0

        for key, value in a_dictionary.items():
            if a_dictionary[key] > max_value:
                max_key = key
                max_value = a_dictionary[key]
    return max_key
