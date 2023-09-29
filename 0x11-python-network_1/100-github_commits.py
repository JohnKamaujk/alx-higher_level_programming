#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


def get_github_commits(owner, repo):
    # Define the GitHub API URL for fetching commits
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        commits_data = response.json()

        # Loop through the commits and print the sha and author name
        for commit in commits_data[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch. Status code: {response.status_code}")


if __name__ == "__main__":
    # Extract the owner and repo names from command line arguments
    owner = sys.argv[2]
    repo = sys.argv[1]

    # Call the function to fetch and display the GitHub commits
    get_github_commits(owner, repo)
