#!/usr/bin/env python3

'''
Module defines a function that returns the list of delays for an
async task
'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Function returns a list of wait times for an async task"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]


if __name__ == '__main__':
    task_wait_n = __import__('4-tasks').task_wait_n

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
