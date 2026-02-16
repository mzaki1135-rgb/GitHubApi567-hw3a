import requests

def get_repos(user_id):
    """
    Fetch a list of repository names for the given GitHub user.
    """
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(
            f"Error fetching repos for user '{user_id}'. "
            f"Status code: {response.status_code}"
        )

    repos_data = response.json()
    return [repo['name'] for repo in repos_data]


def get_commit_count(user_id, repo_name):
    """
    Fetch the number of commits for a given repository.
    """
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(
            f"Error fetching commits for repo '{repo_name}'. "
            f"Status code: {response.status_code}"
        )

    commits_data = response.json()
    return len(commits_data)


def github_user_repo_summary(user_id):
    """
    Return a summary of repositories and their commit counts.
    """
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
    """
    Print the repository summary in the requested format.
    """
    for item in summary:
        print(f"Repo: {item['repo']} Number of commits: {item['commits']}")


# Example usage
if __name__ == "__main__":
    user_id = "mzaki1135-rgb"
    summary = github_user_repo_summary(user_id)
    print_summary(summary)
