#!/usr/bin/env python3
""" Implement wait_random """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for delay and return max_delay"""
    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return (delay)
