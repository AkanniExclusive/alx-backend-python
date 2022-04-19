#!/usr/bin/env python3

'''
Module defines a function that Let's execute multiple coroutines
at the same time with async
'''

from typing import List
import random
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes multiple co-routines asynchronously"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


if __name__ == '__main__':
    wait_n = __import__('1-concurrent_coroutines').wait_n

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
