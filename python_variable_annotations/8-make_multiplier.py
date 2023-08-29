#!/usr/bin/env python3
'''str, int, float for a tuple'''
from typing import Callable
'''make_multiplier function'''


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''The first element of the tuple is the string k. The second
    element is the square of the int/ float v and should
    be annotated as a float'''
    def call(n: float):
        return n * multiplier
    return call
