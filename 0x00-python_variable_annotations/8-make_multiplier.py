#!/usr/bin/env python3
"""Complex types - functions module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
