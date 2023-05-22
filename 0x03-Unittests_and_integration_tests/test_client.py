#!/usr/bin/env python3
"""Test client module."""


import unittest
from unittest.mock import Mock, MagicMock, patch, PropertyMock
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from parameterized import parameterized
from fixtures import TEST_PAYLOAD


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
        """Tests public urls."""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as p:
            p.return_value = {"repos_url": 'abc'}
            a = GithubOrgClient('google')
            self.assertEqual(a._public_repos_url, 'abc')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, a, b, c):
        """Tests repos with license."""
        self.assertEqual(GithubOrgClient.has_license(a, b), c)


if __name__ == "__main__":
    """Main function to run test."""
    unittest.main()
"""
@parametrized_class(('org_payload', 'repos_payload'
, 'expected_repos', 'apache2_repos'), TEST_PATLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with patch('client.requests') as get_patcher:

    def test_public_repos(self):

    def test_public_repos_with_license(self)

    @classmethod
    def tearDownClass(cls):
"""
