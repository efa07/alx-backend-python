#!/usr/bin/env python3
""" Import wait_random from the previous python file.
    The list of the delays should be in ascending order without using sort()
    because of concurrency. """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute multiple coroutines at the same time with async  """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
