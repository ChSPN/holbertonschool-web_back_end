#!/usr/bin/env python3
import asyncio
from typing import List
from 4-main.py import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

# Example usage
if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
