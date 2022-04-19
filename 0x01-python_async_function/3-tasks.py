#!/usr/bin/env python3

'''
Defines a function that returns an asyncio task
'''

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio task"""
    return asyncio.create_task(wait_random(max_delay))


if __name__ == '__main__':
    task_wait_random = __import__('3-tasks').task_wait_random


    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
