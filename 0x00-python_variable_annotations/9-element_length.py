#!/usr/bin/env python3
"""Task 9: Duck typing an iterable object."""
from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each sequence in a list."""
    return [(i, len(i)) for i in lst]
