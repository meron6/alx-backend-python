#!/usr/bin/env python3
"""Test file for task_wait_random function"""
import asyncio

task_wait_random = __import__('2-task_wait_random').task_wait_random

async def main():
    task = task_wait_random(5)
    await task
    print(f"Task result: {task.result()}")

asyncio.run(main())
