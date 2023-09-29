#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
    except Exception as e:
        print(f"Error: {e}")
