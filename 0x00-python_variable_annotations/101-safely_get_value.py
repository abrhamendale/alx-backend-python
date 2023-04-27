#!/usr/bin/env python3
"""Annotations."""


from typing import Mapping, Any, Union, ~T


def safely_get_value(dct: mapping, key: Any, default: Union
                     [~T, None] = None) -> Union[Any, ~T]:
    if key in dct:
        return dct[key]
    else:
        return default
