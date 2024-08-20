#!/usr/bin/env python3
"""
This module contains a coroutine that collects random numbers asynchronously
using async comprehensions.
"""

from typing import List
from 0-async_generator import async_generator  # Correction de l'importation


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from
    async_generator using an async comprehension.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [number async for number in async_generator()][:10]
# Limite à 10 nombres
