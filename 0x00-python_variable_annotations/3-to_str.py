#!/usr/bin/env python3

'''
Defines at type annotated function that returns
the float representation of a string
'''


def to_str(n: float) -> str:
    """Returns the string representation of a float."""
    return str(n)


if __name__ == '__main__':
    to_str = __import__('3-to_str').to_str

    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))#!/usr/bin/env python3

"""
Write a type-annotated function to_str that takes a float n 
as argument and returns the string representation of the float.
"""

def to_str(n: float) -> str:
    return str(n)

print(type(to_str(1.0)))
