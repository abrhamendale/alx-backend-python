#!/usr/bin/env python3
"""Zoom_array"""


from typing import Mapping, Iterable, Union, List, Tuple


def zoom_array(lst: List, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List = [12, 72, 91]

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
