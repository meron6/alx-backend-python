#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes two integer arguments (in this order): n and max_delay.
    An async routine called wait_n.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

# Example usage
if __name__ == "__main__":
    n = 5
    max_delay = 9
    result = asyncio.run(wait_n(n, max_delay))
    print(result)
