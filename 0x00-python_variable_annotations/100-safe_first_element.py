#!/usr/bin/env python3
"""Defines duck typed function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Takes Unknow arg and return any or None"""
    if lst:
        return lst[0]
    else:
        return None
