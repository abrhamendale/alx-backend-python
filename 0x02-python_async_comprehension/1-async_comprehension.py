#!/usr/bin/env python3
"""
Prints 10 random numbers asynchronously.
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Prints 10 random numbers asynchronously."""
    return [i async for i in async_generator()]
