#!/usr/bin/env python3

"""function that measures the total execution
    time for wait_n(n, max_delay)"""

import asyncio
import random
import time
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


def measure_time(n: int, max_delay: int) -> float:
    """function that measures the total execution
    time for wait_n(n, max_delay)"""

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
