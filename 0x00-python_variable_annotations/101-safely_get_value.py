#!/usr/bin/env python3
"""Safely get value module"""
from typing import Union, Any, TypeVar, Mapping


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value of a key in a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default

