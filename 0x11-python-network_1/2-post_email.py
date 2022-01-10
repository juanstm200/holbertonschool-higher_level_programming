#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL """


import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email).encode('ascii')
    arg = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(arg) as response:
        content = response.read().decode('utf-8')
    print(content)
