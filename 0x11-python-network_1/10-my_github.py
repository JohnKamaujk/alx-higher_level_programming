#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import sys
import requests


def get_github_id(username, personal_access_token):
    # Define the GitHub API URL for user information
    url = f'https://api.github.com/users/{username}'

    # Create a Basic Authentication header
    auth = (username, personal_access_token)

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=auth)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and extract the user id
        user_data = response.json()
        github_id = user_data.get('id')
        return github_id


if __name__ == "__main__":
    # Extract the username and personal access token
    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    # Call the function to get the GitHub user id and display it
    github_id = get_github_id(username, personal_access_token)
    print(github_id)
