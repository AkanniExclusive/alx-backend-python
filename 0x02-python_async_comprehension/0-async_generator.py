#!/usr/bin/env python3

'''
Module defines a coroutine that loops asynchronously.
'''

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops asynchronously 10 times waiting for 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10


if __name__ == '__main__':
    async_generator = __import__('0-async_generator').async_generator

    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
