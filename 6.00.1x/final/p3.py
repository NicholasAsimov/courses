#!/bin/python2


def dict_invert(d):
    inverted = {}

    for key, val in d.items():
        if val in inverted:
            inverted[val].append(key)
            inverted[val].sort()
        else:
            inverted[val] = [key]

    return inverted


# Test Cases
d = {1: 10, 2: 20, 3: 30}
print dict_invert(d) == {10: [1], 20: [2], 30: [3]}

d = {1: 10, 2: 20, 3: 30, 4: 30}
print dict_invert(d) == {10: [1], 20: [2], 30: [3, 4]}

d = {4: True, 2: True, 0: True}
print dict_invert(d) == {True: [0, 2, 4]}

d = {30000: 30, 600: 30, 2: 10}
print dict_invert(d) == {10: [2], 30: [600, 30000]}
