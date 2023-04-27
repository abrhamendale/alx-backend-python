#!/usr/bin/env python3
"""sum_mixed_list"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Adds elements of a mixed list."""
    s: float = 0
    for i in mxd_list:
        s = s + i
    return (s)
