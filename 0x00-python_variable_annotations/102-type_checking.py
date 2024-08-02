#!/usr/bin/env python3
"""Task 12: Type Checking"""
from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Creates multiple copies of items in a tuple."""
    zoomed_in: List[int] = [
        item for item in lst for _ in range(factor)
    ]
    return zoomed_in

array: Tuple[int, ...] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
