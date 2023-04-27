#!/usr/bin/env python3
"""Sum_list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums elements of a list."""
    s: float = 0
    for i in input_list:
        s = s + i
    return (s)
