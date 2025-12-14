import requests

def extract_repo_info(repo_url):
    """
    Extract username and repo name from GitHub URL
    """
    parts = repo_url.replace("https://github.com/", "").split("/")
    if len(parts) < 2:
        return None, None
    return parts[0], parts[1]

def fetch_repo_data(repo_url):
    username, repo_name = extract_repo_info(repo_url)

    if not username or not repo_name:
        return None

    repo_api = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(repo_api)

    if response.status_code != 200:
        return None

    data = response.json()

    commit_count = fetch_commit_count(username, repo_name)

    repo_data = {
        "name": data.get("name"),
        "description": data.get("description"),
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "language": data.get("language"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
        "commits": commit_count
    }

    return repo_data


def fetch_commit_count(username, repo_name):
    commits_api = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    response = requests.get(commits_api)

    if response.status_code != 200:
        return 0

    commits = response.json()
    return len(commits)
