#!/usr/bin/python3
"""Async module"""


import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    "Returns a random number between 0 and max_delay"
    r = random.uniform(0, max_delay)
    s = time.perf_counter()
    await asyncio.sleep(r)
    return (r)
