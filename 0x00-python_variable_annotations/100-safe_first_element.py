#!/usr/bin/env python3
"""Duck typing - first element of a sequence module"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Union[int, float, Any]]) -> Union[int, float, Any]:
    """Return the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
