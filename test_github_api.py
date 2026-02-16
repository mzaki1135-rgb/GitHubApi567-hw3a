import unittest
from github_api import get_repos, get_commit_count, github_user_repo_summary


class TestGitHubApi(unittest.TestCase):

    def test_get_repos_valid_user(self):
        repos = get_repos("mzaki1135-rgb")
        self.assertIsInstance(repos, list)
        self.assertGreaterEqual(len(repos), 0)

    def test_get_repos_invalid_user(self):
        with self.assertRaises(ValueError):
            get_repos("thisuserdoesnotexist_1234567890")

    def test_get_commit_count_valid_repo(self):
        repos = get_repos("mzaki1135-rgb")

        # Only run test if user has at least one repo
        if repos:
            count = get_commit_count("mzaki1135-rgb", repos[0])
            self.assertIsInstance(count, int)
            self.assertGreaterEqual(count, 0)

    def test_summary_function(self):
        summary = github_user_repo_summary("mzaki1135-rgb")
        self.assertIsInstance(summary, list)

        for item in summary:
            self.assertIn("repo", item)
            self.assertIn("commits", item)
            self.assertIsInstance(item["commits"], int)

if __name__ == "__main__":
    unittest.main()
