#!/usr/bin/env python3
"""Function annotation"""


from typing import Callable


def func(b: float):
    """Multiplier function"""
    return 3 * b


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies."""
    return func(multiplier)
