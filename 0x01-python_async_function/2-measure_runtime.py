#!/usr/bin/env python3
"""Measure the runtime for wait_n(n, max_delay)"""

from time import perf_counter
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns average time per execution.
    Args:
        n (int): Number of times to execute the function.
        max_delay (int): Maximum delay for wait_n.
    Returns:
        float: Average time per execution.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n

# Example usage
if __name__ == "__main__":
    n = 5
    max_delay = 9
    avg_time = measure_time(n, max_delay)
    print(avg_time)
