#!/usr/bin/env python3

'''
Defines a function that measures the total execution time
for the program.
'''

import asyncio
from time import perf_counter
import random


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for the program"""
    s = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - s
    return elapsed


if __name__ == '__main__':
    measure_time = __import__('2-measure_runtime').measure_time

    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
