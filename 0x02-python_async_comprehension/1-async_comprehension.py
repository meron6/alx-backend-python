#!/usr/bin/env python3
"""A Python module that returns 10 random numbers using async comprehension."""
from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    async_comprehension - a function that returns 10 random numbers.
    Arguments:
        None
    Returns:
        A list of 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
