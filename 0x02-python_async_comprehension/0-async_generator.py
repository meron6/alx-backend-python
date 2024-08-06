#!/usr/bin/env python3
"""An asynchronous generator that yields random numbers."""

import asyncio
import random

async def async_generator() -> AsyncIterator[float]:
    """
    An asynchronous generator that yields 10 random numbers between 0 and 10,
    waiting 1 second between each yield.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
