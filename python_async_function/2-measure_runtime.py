#!/usr/bin/env python3
import asyncio
import time
from 1-main.py import (
    wait_n,
)  # Replace 'previous_file' with the actual filename


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n


# Example usage
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
