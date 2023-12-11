#!/usr/bin/env python3
"""Define make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that mulitplies a float"""
    def multiplyFloat(Float):
        return (Float * multiplier)

    return (multiplyFloat)
