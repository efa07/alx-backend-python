#!/usr/bin/env python3
"""
This script contains a client for fetching data from the GitHub API
and unit tests for the client.
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
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with
        (f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(result, {"key": "value"})

    @patch.object(GithubOrgClient, 'org', return_value={"repos_url": "https://api.github.com/orgs/google/repos"})
    def test_public_repos_url(self, mock_org):
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")
        mock_org.assert_called_once()

    @patch('github_client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', return_value='https://api.github.com/orgs/google/repos')
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        mock_get_json.return_value = [
            {"name": "repo1", "url": "https://api.github.com/repos/google/repo1"},
            {"name": "repo2", "url": "https://api.github.com/repos/google/repo2"}
        ]

        client = GithubOrgClient("google")
        result = client.public_repos()

        expected_result = [
            {"name": "repo1", "url": "https://api.github.com/repos/google/repo1"},
            {"name": "repo2", "url": "https://api.github.com/repos/google/repo2"}
        ]

        self.assertEqual(result, expected_result)
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with('https://api.github.com/orgs/google/repos')

if __name__ == '__main__':
    unittest.main()
