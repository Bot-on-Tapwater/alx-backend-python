#!/usr/bin/env python3
"""Implement async_generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yield rand no 0 - 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
