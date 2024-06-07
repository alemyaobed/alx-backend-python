#!/usr/bin/env python3
'''
Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.
'''


def floor(n: float) -> float:
    ''' Returns the floor of a float'''
    from math import floor as f
    return f(n)
