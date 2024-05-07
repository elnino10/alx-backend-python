#!/usr/bin/env python3
"""Async Generator Module"""
import asyncio
from typing import AsyncGenerator
from random import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Async Generator that yields a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield 10 * random()
