#!/usr/bin/env python3

'''
Defines a type annotated functions that concatenates 2 strings
'''


def concat(str1: str, str2: str) -> str:
    """returns concatenated string"""
    return str1 + str2


if __name__ == '__main__':
    concat = __import__('1-concat').concat

    str1 = "egg"
    str2 = "shell"

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)#!/usr/bin/env python3
"""
Write a type-annotated function concat that takes a string 
str1 and a string str2 as arguments and returns a concatenated string
"""

def concat(str1: str, str2:str)->str:
    return str1 + str2
