#!/usr/bin/env python3
"""transform in new def task and return list of delay"""

import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random
"""import task_wait_random from 3-tasks"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
