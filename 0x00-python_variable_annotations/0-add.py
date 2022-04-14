#!/usr/bin/env python3

'''
Defines a type annotated functions that returns sum of two floats
'''


def add(a: float, b: float) -> float:
    """Returns the sum of two floats as a float"""
    return a + b


if __name__ == '__main__':
    add = __import__('0-add').add

    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
