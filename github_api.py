import requests

def get_user_repos(user_id, request_get=requests.get):
    """
    Given a GitHub user ID, return a list of
    (repo_name, number_of_commits) tuples.
    """

    repos_url = f"https://api.github.com/users/{user_id}/repos"

    response = request_get(repos_url)

    if response.status_code != 200:
        raise ValueError("Invalid GitHub user or API error")

    repos = response.json()

    result = []

    for repo in repos:
        repo_name = repo["name"]

        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = request_get(commits_url)

        if commits_response.status_code != 200:
            raise ValueError("Error retrieving commits")

        commits = commits_response.json()
        result.append((repo_name, len(commits)))

    return result
