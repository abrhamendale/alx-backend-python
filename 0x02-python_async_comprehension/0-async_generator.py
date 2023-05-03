#!/usr/bin/env python3
"""
Returns a random list of 10 numbers.
"""


import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """Generates a random number between 0 and 10."""
    r = []
    for i in range(0, 10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
