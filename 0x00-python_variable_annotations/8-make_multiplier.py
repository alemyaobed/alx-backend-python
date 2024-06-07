#!/usr/bin/env python3
'''
Write a type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Takes a float multiplier and returns a function that mulitplies a float
    by the multiplier
    '''
    def multiplier_function(value: float) -> float:
        '''The callable function that does the multiplication'''
        return multiplier * value
    return multiplier_function
