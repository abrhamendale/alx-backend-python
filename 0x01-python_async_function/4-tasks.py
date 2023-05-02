#!/usr/bin/env python3
"""Task_1"""


import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 0) -> List[float]:
    """Returns the list of all delays."""
    ret = []
    for i in range(0, n):
        tsk = await task_wait_random(max_delay)
        while True:
            if tsk.done():
                print(tsk.result(), "Output")
                ret.append(tsk.result())
                break
    return (sorted(ret))
