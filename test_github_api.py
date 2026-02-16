import unittest
from unittest.mock import patch, Mock
from github_api import get_repos, get_commit_count, github_user_repo_summary


class TestGitHubApi(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_get_repos(self, mock_get):
        # Mock response for repository list
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]
        mock_get.return_value = mock_response

        repos = get_repos("anyuser")
        self.assertEqual(repos, ["Repo1", "Repo2"])


    @patch("github_api.requests.get")
    def test_get_commit_count(self, mock_get):
        # Mock response for commits
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"sha": "abc"},
            {"sha": "def"},
            {"sha": "ghi"}
        ]
        mock_get.return_value = mock_response

        count = get_commit_count("anyuser", "Repo1")
        self.assertEqual(count, 3)


    @patch("github_api.requests.get")
    def test_summary_function(self, mock_get):
        # Side effect to simulate different URLs
        def mock_side_effect(url, *args, **kwargs):
            mock_response = Mock()
            mock_response.status_code = 200

            if "repos" in url:
                mock_response.json.return_value = [
                    {"name": "RepoA"},
                    {"name": "RepoB"}
                ]
            elif "commits" in url:
                mock_response.json.return_value = [
                    {"sha": "1"},
                    {"sha": "2"}
                ]
            return mock_response

        mock_get.side_effect = mock_side_effect

        summary = github_user_repo_summary("anyuser")

        expected = [
            {"repo": "RepoA", "commits": 2},
            {"repo": "RepoB", "commits": 2}
        ]

        self.assertEqual(summary, expected)


if __name__ == "__main__":
    unittest.main()
