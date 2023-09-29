#!/usr/bin/python3
"""A script that fetches url using the requests library."""

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
