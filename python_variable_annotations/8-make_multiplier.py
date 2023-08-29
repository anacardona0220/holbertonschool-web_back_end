#!/usr/bin/env python3
'''import callable'''
from typing import Callable
'''make_multiplier function'''


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Write a type-annotated function make_multiplier that takes
    a float multiplier as argument and returns a function that
    multiplies a float by multiplier.'''
    def call(n: float):
        return n * multiplier
    return call
