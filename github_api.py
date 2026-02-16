"""
GitHub API Assignment HW03
Author: mzaki1135-rgb
"""

import requests

def get_repos(user_id):
    """Fetch the list of repositories for a given GitHub user."""
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error fetching repos for user '{user_id}'. Status code: {response.status_code}")
    repos_data = response.json()
    return [repo['name'] for repo in repos_data]

def get_commit_count(user_id, repo_name):
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error fetching commits for repo '{repo_name}'. Status code: {response.status_code}")
    commits_data = response.json()
    return len(commits_data)

def github_user_repo_summary(user_id):
    summary = []
    try:
        repos = get_repos(user_id)
        for repo in repos:
            count = get_commit_count(user_id, repo)
            summary.append({'repo': repo, 'commits': count})
    except ValueError as e:
        print(e)
    return summary

def print_summary(summary):
    """Print the repository summary in the requested format."""
    for item in summary:
        print(f"Repo: {item['repo']} Number of commits: {item['commits']}")

# Example usage
if __name__ == "__main__":
    user_id = "richkempinski"  # Replace with any GitHub user to test
    summary = github_user_repo_summary(user_id)
    print_summary(summary)
