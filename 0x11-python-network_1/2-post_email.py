#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode("ascii")
    req = urllib.request.Request(url, data=data, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except Exception as e:
        print(f"Error: {e}")
