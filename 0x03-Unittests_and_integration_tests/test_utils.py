#!/usr/bin/env python3
"""
Test module for access_nested_map
"""


import unittest
from unittest.mock import MagicMock, patch
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test functions class"""

    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, {"a", }),
        ({"a": 1}, {"a", "b"})
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test function for exceptions."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Json test class."""

    """@parametrized.expand([
        ('http://example.com', True),
        ('http://holberton.io', False)
    ])"""
    @patch('utils.requests')
    def test_get_json(self, mock_requests):
        """Test json functions."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = True
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_json('http://example.com'), True)
        mock_response.json.return_value = False
        self.assertEqual(get_json('http://holberton.io'), False)


if __name__ == "__main__":
    """Main function to run test."""
    unittest.main()
