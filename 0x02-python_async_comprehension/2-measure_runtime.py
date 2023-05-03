#!/usr/bin/env python3
"""
Measures the time to execute "async_comprehension" function 4 times.
"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures runtime."""
    t1 = time.perf_counter()
    asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    return (time.perf_counter() - t1)
