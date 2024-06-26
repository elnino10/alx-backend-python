#!/usr/bin/env python3
"""Async Generator Module"""
import asyncio
from typing import Generator
from random import random


async def async_generator() -> Generator[float, None, None]:
    """Async Generator that yields a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield 10 * random()
