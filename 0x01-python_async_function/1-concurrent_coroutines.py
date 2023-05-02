#!/usr/bin/env python3
"""Task_1"""


import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 0) -> List[float]:
    """Returns the list of all delays."""
    ret = []
    for i in range(0, n):
        ret.append(await wait_random(max_delay))
    return (sorted(ret))
