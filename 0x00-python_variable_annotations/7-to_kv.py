#!/usr/bin/env python3
"""Define function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of k & v"""
    return (k, float(v * v))
