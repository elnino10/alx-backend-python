#!/usr/bin/env python3
"""Async Comprehension Module"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """Collect 10 random numbers using an async generator"""
    return [num async for num in async_generator()]
