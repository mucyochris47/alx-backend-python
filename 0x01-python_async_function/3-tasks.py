#!/usr/bin/env python3
"""3. Tasks"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that waits for a random amount of time.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio.Task object representing the task.
    """
    return asyncio.create_task(wait_random(max_delay))
