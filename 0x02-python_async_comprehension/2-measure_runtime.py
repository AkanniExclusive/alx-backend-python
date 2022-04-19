#!/usr/bin/env python3

'''
Defines a function that runs a task 4 times in parallel
and calculates the run-time
'''

import asyncio
from typing import List
from time import perf_counter


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes 4 tasks in parallel and calculates their run-time
    """
    i = perf_counter()
    task = [asyncio.create_task(async_comprehension()) for j in range(4)]
    await asyncio.gather(*task)
    elapsed_time = perf_counter() - i
    return elapsed_time


if __name__ == '__main__':
    measure_runtime = __import__('2-measure_runtime').measure_runtime


    async def main():
        return await(measure_runtime())

    print(
        asyncio.run(main())
    )
