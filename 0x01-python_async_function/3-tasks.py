#!/usr/bin/env python3
"""Task_3"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """Returns an async function."""
    if max_delay < 0:
        return (None)
    return (asyncio.create_task(wait_random(max_delay)))
