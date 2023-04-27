#!/usr/bin/env python3
"""Duck typing."""
# The types of the elements of the input are not know


from typing import Sequence, Iterable, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of the list."""
    if lst:
        return lst[0]
    else:
        return None
