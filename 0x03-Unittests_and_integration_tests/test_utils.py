#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function using unittest and parameterized.
"""

import functools
import requests
import unittest
from unittest.mock import patch, Mock


def get_json(url):
    response = requests.get(url)
    return response.json()


def memoize(func):
    @functools.wraps(func)
    def wrapper(self):
        if not hasattr(self, '_cache'):
            self._cache = {}
        if func.__name__ not in self._cache:
            self._cache[func.__name__] = func(self)
        return self._cache[func.__name__]
    return wrapper


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestClass:
    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        test_instance = TestClass()

        # Call the memoized property twice
        first_call = test_instance.a_property
        second_call = test_instance.a_property

        # Check that the result is correct
        self.assertEqual(first_call, 42)
        self.assertEqual(second_call, 42)

        # Check that a_method was called only once
        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
