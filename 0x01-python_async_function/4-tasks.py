#!/usr/bin/env python3
""" Implement wait_random """
import asyncio


async def wait_random(max_delay: int) -> int:
    """Wait for delay and return max_delay"""
    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return (delay)
