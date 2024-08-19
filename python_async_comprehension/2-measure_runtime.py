#!/usr/bin/env python3
"""
This module contains a coroutine that measures the runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import List
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of running async_comprehension
    four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()  # Record the start time

    # Run async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()  # Record the end time

    return end_time - start_time  # Calculate and return the total runtime
