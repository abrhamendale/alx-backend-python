#!/usr/bin/env python3
"""
Test module for access_nested_map
"""


import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""
    
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, "a", "b", 2)
    ])
    def test_access_nested_map(self):
        """Test function."""
        assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == "__main__":
    unittest.main()
