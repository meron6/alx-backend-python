#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer argument."""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay (included) seconds and return the delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay time.
    """
    new_rand = random.uniform(0, max_delay)
    await asyncio.sleep(new_rand)
    return new_rand
