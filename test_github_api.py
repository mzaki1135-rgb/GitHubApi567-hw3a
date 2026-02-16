import unittest
from github_api import get_repos, get_commit_count, github_user_repo_summary

class TestGitHubApi(unittest.TestCase):

    def test_get_repos_valid_user(self):
        repos = get_repos("richkempinski")
        self.assertIsInstance(repos, list)
        self.assertIn("hellogitworld", repos)

    def test_get_repos_invalid_user(self):
        with self.assertRaises(ValueError):
            get_repos("thisuserdoesnotexist12345")

    def test_get_commit_count_valid_repo(self):
        count = get_commit_count("richkempinski", "hellogitworld")
        self.assertIsInstance(count, int)
        self.assertGreaterEqual(count, 0)

    def test_summary_function(self):
        summary = github_user_repo_summary("richkempinski")
        self.assertIsInstance(summary, list)
        if summary:
            self.assertIn("repo", summary[0])
            self.assertIn("commits", summary[0])

if __name__ == "__main__":
    unittest.main()
