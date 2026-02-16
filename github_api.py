import requests

def get_repos(mzaki1135-rgb):

    url = f"https://api.github.com/users/mzaki1135-rgb/repos"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error fetching repos for user 'mzaki1135-rgb'. Status code: {response.status_code}")
    repos_data = response.json()
    return [repo['GitHubApi567-hw3a'] for repo in repos_data]

def get_commit_count(mzaki1135-rgb, GitHubApi567-hw3a):
    url = f"https://api.github.com/repos/mzaki1135-rgb/GitHubApi567-hw3a/commits"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error fetching commits for repo 'GitHubApi567-hw3a'. Status code: {response.status_code}")
    commits_data = response.json()
    return len(commits_data)

def github_user_repo_summary(mzaki1135-rgb):
    summary = []
    try:
        repos = get_repos(mzaki1135-rgb)
        for repo in repos:
            count = get_commit_count(mzaki1135-rgb, repo)
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
    user_id = "mzaki1135-rgb" 
    summary = github_user_repo_summary(user_id)
    print_summary(summary)
