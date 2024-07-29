#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function using unittest and parameterized.
"""

import requests
import unittest
from unittest.mock import patch, Mock


def get_json(url):
    response = requests.get(url)
    return response.json()


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


if __name__ == '__main__':
    unittest.main()
