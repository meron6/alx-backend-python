#!/usr/bin/env python3
"""Task 6: Complex types - mixed list."""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Compute the sum of a list containing both integers and floating-point numbers."""
    return sum(mxd_lst)
