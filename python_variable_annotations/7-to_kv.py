#!/usr/bin/env python3
from typing import Union, Tuple
'''to_kv function'''


def to_kv(k: str, v: Union[int, float] ) -> Tuple[str, float]:
    '''retur k and square v'''
    return (k, v * v)
