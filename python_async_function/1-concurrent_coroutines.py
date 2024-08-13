#!/usr/bin/env python3
import asyncio
from typing import List
from 1-main.py import (
    wait_random,
)  # wait_random is a coroutine that takes in an integer argument and returns a float.


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)


# Example usage
if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
