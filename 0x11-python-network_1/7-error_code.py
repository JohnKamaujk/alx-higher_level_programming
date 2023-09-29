#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response.
"""

import requests
import sys


def display_response(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check the HTTP status code
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    # Extract the URL from the command line argument
    url = sys.argv[1]

    # Call the function to send the request and display the response
    display_response(url)
