#!/usr/bin/env python3
"""Annotate a function."""


from typing import List, Tuple, Union, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
