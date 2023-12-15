#!/usr/bin/env python3
"""Implement measure_runtime"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure total runtime"""
    startTime = time.time()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    endTime = time.time()

    elapsedTime = endTime - startTime

    return elapsedTime
