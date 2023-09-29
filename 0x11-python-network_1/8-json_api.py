#!/usr/bin/python3
"""A script that
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys


def search_user(letter):
    # Define the URL and parameters for the POST request
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': letter}

    # Send the POST request
    response = requests.post(url, data=params)

    try:
        # Parse the JSON response
        data = response.json()

        # Check if the JSON response is not empty
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    # Check if an argument is provided, otherwise set letter to an empty string
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    # Call the function to send the POST request and display the response
    search_user(letter)
