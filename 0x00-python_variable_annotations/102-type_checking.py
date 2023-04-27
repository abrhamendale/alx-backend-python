#!/usr/bin/env python3
"""Zoom_array"""


from typing import Mapping, Iterable, Union, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = [12, 72, 91]

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3.0)
