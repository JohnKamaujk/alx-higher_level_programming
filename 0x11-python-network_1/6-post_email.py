#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""

import requests
import sys


def send_post_request(url, email):
    # Define the data to be sent in the POST request
    data = {'email': email}

    # Send the POST request
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)


if __name__ == "__main__":
    # Extract the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the function to send the POST request and display the response
    send_post_request(url, email)
