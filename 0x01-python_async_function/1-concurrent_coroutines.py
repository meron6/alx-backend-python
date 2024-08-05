#!/usr/bin/env python3

import asyncio
import heapq
from typing import List
from _basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the list of delays sorted in ascending order.

    Args:
        n (int): Number of times to spawn the wait_random coroutine.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays sorted in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return list(heapq.nsmallest(len(delays), delays))
