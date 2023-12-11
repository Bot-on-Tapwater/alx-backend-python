#!/usr/bin/env python3
"""Define sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of floats and ints"""
    return float(sum(mxd_lst))
