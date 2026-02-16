import unittest
from unittest.mock import patch, MagicMock
from github_api import get_user_repos


class TestGitHubApi(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_valid_user(self, mock_get):

        repo_response = MagicMock()
        repo_response.status_code = 200
        repo_response.json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]

        commit_response_1 = MagicMock()
        commit_response_1.status_code = 200
        commit_response_1.json.return_value = [1, 2, 3]

        commit_response_2 = MagicMock()
        commit_response_2.status_code = 200
        commit_response_2.json.return_value = [1, 2]

        mock_get.side_effect = [
            repo_response,
            commit_response_1,
            commit_response_2
        ]

        result = get_user_repos("testuser")

        self.assertEqual(result, [
            ("Repo1", 3),
            ("Repo2", 2)
        ])

    @patch("github_api.requests.get")
    def test_invalid_user(self, mock_get):

        error_response = MagicMock()
        error_response.status_code = 404

        mock_get.return_value = error_response

        with self.assertRaises(ValueError):
            get_user_repos("invaliduser")


if __name__ == "__main__":
    unittest.main()
