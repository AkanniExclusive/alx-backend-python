#!/usr/bin/env python3

'''
Defines a type annotated function that takes a string k
and an int OR a float v as arguments and returns a tuple.
'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and a float/integer and returns a tuple"""
    return (k, v * v)


if __name__ == '__main__':
    to_kv = __import__('7-to_kv').to_kv

    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
