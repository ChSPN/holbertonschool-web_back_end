#!/usr/bin/env python3
import asyncio
from typing import List
from previous_file import (
    wait_random,
)  # Replace 'previous_file' with the actual filename


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)


# Example usage
if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
