#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for `n` random delays and returns a sorted list of the delays.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay value.

    Returns:
        List[int]: A sorted list of the delays.
    """
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn
    return delay_list
