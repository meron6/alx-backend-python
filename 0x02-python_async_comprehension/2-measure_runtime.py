#!/usr/bin/env python3
"""Measure the runtime for executing async_comprehension in parallel."""

import asyncio
import time
from _async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Measure the total runtime for executing async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
