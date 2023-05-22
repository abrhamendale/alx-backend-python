#!/usr/bin/env python3
"""
Test module for access_nested_map
"""


import unittest
from unittest.mock import Mock, MagicMock, patch
from utils import access_nested_map, get_json, memoize
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
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = True
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_json('http://example.com'), True)
        mock_requests.get.assert_called_once_with('http://example.com')
        mock_response.json.return_value = False
        self.assertEqual(get_json('http://holberton.io'), False)


class TestMemoize(unittest.TestCase):
    """Memoize test class."""

    def test_memoize(self):
        """A memoize test function."""

        class TestClass():
            """ A class inside a method."""

            def a_method(self):
                """A method."""
                return 42

            @memoize
            def a_property(self, a):
                return self.a_method()
        t = TestClass()
        with patch('test_utils.TestMemoize.TestClass') as p:
            p.a_method.return_value = 42
            self.assertEqual(TestClass.a_property, 42)
            self.assertEqual(TestClass.a_property, 42)
            a_mock.assert_called_once()

if __name__ == "__main__":
    """Main function to run test."""
    unittest.main()
