#!/usr/bin/env python3
""" This module contains a coroutine that collects
random numbers asynchronously using async comprehensions. """
import asyncio
import time

# Importation directe de la fonction
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    # Exécuter async_comprehension quatre fois en parallèle
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()
    return end_time - start_time
