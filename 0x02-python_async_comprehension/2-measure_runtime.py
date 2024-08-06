#!/usr/bin/env python3
"""A Python module to measure execution time."""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Executes async_comprehension four times and measures the total execution time.
    Returns:
        The total time taken to complete the task.
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return (end_time - start_time)
