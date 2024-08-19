#!/usr/bin/env python3
"""
This module contains a coroutine that generates random numbers asynchronously.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
Coroutine that yields 10 random numbers between 0 and 10 asynchronously.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
