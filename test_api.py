import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USER = os.getenv("GITHUB_USER")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_repo():
    url = f"https://api.github.com/user/repos"
    data = {"name": REPO_NAME, "auto_init": True, "private": False}
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"Repository {REPO_NAME} created successfully.")
    else:
        print(f"Failed to create repository: {response.json()['message']}")

def check_repo_exists():
    url = f"https://api.github.com/users/{GITHUB_USER}/repos"
    response = requests.get(url, headers=HEADERS)
    repos = response.json()
    if any(repo["full_name"] == f"{GITHUB_USER}/{REPO_NAME}" for repo in repos):
        print(f"Repository {REPO_NAME} exists.")
    else:
        print(f"Repository {REPO_NAME} does not exist.")

def delete_repo():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Repository {REPO_NAME} deleted successfully.")
    else:
        print(f"Failed to delete repository: {response.json()['message']}")

def main():
    create_repo()
    check_repo_exists()
    delete_repo()
    check_repo_exists()

if __name__ == "__main__":
    main()