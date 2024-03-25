#!/usr/bin/python3

def number_keys(a_dictionary):
    key_count = 0
    for k, v in a_dictionary.items():
        key_count += 1
    return key_count
