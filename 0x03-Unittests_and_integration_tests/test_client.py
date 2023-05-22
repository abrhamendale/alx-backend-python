#!/usr/bin/env python3
"""Test client module."""


import unittest
from unittest.mock import Mock, MagicMock, patch, PropertyMock
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """A class for testing git client."""

    @parameterized.expand([
        ('google', True),
        ('abc', True)
    ])                        
    @patch('client.get_json')
    def test_org(self, expected, url, m_requests):
        """Tests git org."""
        mock_response = Mock()
        mock_response.return_value = 'abcd'
        m_requests.return_value = mock_response
        self.assertEqual(GithubOrgClient(url).org(), 'abcd')
        m_requests.assert_called_once()

    def test_public_repos_url(self):
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as p:
            p.return_value = { "repos_url": 'abc' }
            a = GithubOrgClient('google')
            self.assertEqual(a._public_repos_url, 'abc')#'https://api.github.com/orgs/google/repos')

    #@patch('utils.get_json')
    #def test_public_repos(self, g_mock):
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, a, b, c):
        self.assertEqual(GithubOrgClient.has_license(a, b), c)

