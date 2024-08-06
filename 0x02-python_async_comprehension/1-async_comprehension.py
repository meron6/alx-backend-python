#!/usr/bin/env python3
"""Collect random numbers using async comprehension from async_generator."""

from typing import List
from _async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [number async for number in async_generator()]
