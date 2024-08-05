#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n"""
import asyncio
from typing import list

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> list[float]:
"""
it into a new function task_wait_n
identical to wait_n except task_wait_random
"""
tasks = [task_wiat_random(max_delay) for - in range(n)]
return [awit task for task in asyncio.as_completed(tasks)]
