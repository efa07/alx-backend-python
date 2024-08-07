#!/usr/bin/env python3
""" From the previous file, import wait_n into 2-measure_runtime.py.
    Create a measure_time function with integers n and max_delay as arguments
    and returns total_time / n. """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure runtime """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
