#!/usr/bin/env python3
"""Implement wait_n"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """return list of delays"""
    delays = [await wait_random(max_delay) for i in range(0, n)]

    return delays
