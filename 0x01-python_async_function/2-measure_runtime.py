#!/usr/bin/env python3
"""Task_2"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int = 1, max_delay: int = 0) -> float:
    """Returns the average execution time."""
    if n < 0 or max_delay < 0:
        return (0)
    t1 = time.perf_counter()
    await wait_n(n, max_delay)
    if n > 0:
        return ((time.perf_counter() - t1) / n)
    else:
        return (time.perf_counter() - t1)
