#!/usr/bin/env python3
"""
This script contains a client for fetching data from the GitHub API and unit tests for the client.
The client is designed to fetch organization details using the GitHub API.

Functions:
    get_json(url): Fetches JSON data from a given URL.

Classes:
    GithubOrgClient: Client for fetching GitHub organization details.
    TestGithubOrgClient: Unit tests for the GithubOrgClient class.
"""


import unittest
from unittest.mock import patch
from parameterized import parameterized


def get_json(url):
    """
    Fetches JSON data from a given URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        dict: The JSON data fetched from the URL.
    """
    pass


class GithubOrgClient:
    """
    Client for fetching GitHub organization details.

    Args:
        org_name (str): The name of the GitHub organization.
    """
    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        """
        Fetches the organization details from GitHub.

        Returns:
            dict: The organization details.
        """
        return get_json(f'https://api.github.com/orgs/{self.org_name}')

class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('github_client.get_json', return_value={"key": "value"})
    def test_org(self, org_name, mock_get_json):
        """
        Tests that GithubOrgClient.org returns the correct value.

        Args:
            org_name (str): The name of the GitHub organization.
            mock_get_json (Mock): The mocked get_json function.
        """
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(result, {"key": "value"})

if __name__ == '__main__':
    unittest.main()
