#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function using unittest and parameterized.
"""

import unittest
from parameterized import parameterized


def access_nested_map(nested_map, path):
    """
    Accesses a value in a nested dictionary using a tuple path.

    Args:
        nested_map (dict): The nested dictionary to traverse.
        path (tuple): A tuple representing the path of keys to follow.

    Returns:
        The value found at the end of the path in the nested dictionary.

    Raises:
        KeyError: If a key in the path is not found in the nested dictionary.
    """
    for key in path:
        nested_map = nested_map[key]
    return nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
