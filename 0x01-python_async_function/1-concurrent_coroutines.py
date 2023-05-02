#!/usr/bin/env python3
"""Task_1"""


wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
import random


async def wait_n(n: int, amx_delay: int) -> List[float]:
    """Returns the list of all delays."""

