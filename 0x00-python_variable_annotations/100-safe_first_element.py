#!/usr/bin/env python3
"""
Augment the following code with the
correct duck-typed annotations
"""
from typing import TypeVar, Any, Union, Mapping, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """func that returns the first element if an iterable is passed, else None
     """
    if lst:
        return lst[0]
    else:
        return None
