#!/usr/bin/env python3
"""Annotate element_length function"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ No docstrings """
    return [(i, len(i)) for i in lst]
