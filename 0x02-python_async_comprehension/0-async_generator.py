#!/usr/bin/env python3
"""Creates a generator"""
import asyncio
from typing import Generator
import random


async def async_generator():
    """waits 1 second then yield a random number between 0 and 10"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
