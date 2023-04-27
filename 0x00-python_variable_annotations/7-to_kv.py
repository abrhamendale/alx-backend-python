#!/usr/bin/env python3
"""Returns a tuple"""


from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a float from the input arguments."""
    return (k, v * v)
