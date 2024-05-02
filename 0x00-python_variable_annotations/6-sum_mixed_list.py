#!/usr/bin/env python3
"""Complex types - mixed list module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of floats and integers"""
    return sum(mxd_lst)
