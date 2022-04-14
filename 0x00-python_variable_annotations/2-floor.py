#!/usr/bin/env python3

'''
Defines a type annotated functions that takes a
float and returns the floor value of the float.
'''
import math


def floor(n: float) -> int:
    """returns the floor value of the float"""
    return math.floor(n)


if __name__ == '__main__':
    floor = __import__('2-floor').floor

    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
