#!/usr/bin/env python3
"""Task 11: More involved type annotations."""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Retrieve a value from a dictionary using a specified key."""
    return dct[key] if key in dct else default
