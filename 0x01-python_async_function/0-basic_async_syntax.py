#!/usr/bin/env python3

'''
Module defines a function that waits for a random delay
time, then returns a random number
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for random delay between 0 and max_delay and
    returns the value of the random number.
    """
    random_num = random.random() * max_delay
    await asyncio.sleep(random_num)
    return random_num


if __name__ == '__main__':
    wait_random = __import__('0-basic_async_syntax').wait_random

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
